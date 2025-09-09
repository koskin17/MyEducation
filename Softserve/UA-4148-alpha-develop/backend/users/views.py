import logging
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)
from rest_framework_simplejwt.tokens import RefreshToken

# Get logger for this module
logger = logging.getLogger(__name__)

from users.serializers import (
    PasswordResetRequestSerializer,
    PasswordResetSubmissionSerializer,
    TokenVerificationSerializer,
    UserRegistrationSerializer,
    UserRoleSerializer,
    UserSerializer,
)
from users.utils.email_activation import (
    generate_activation_token,
    verify_activation_token,
)
from users.utils.email_utils import send_activation_email

from .models import UserProfile, UserRole
from .permissions import InvestorRolePermission
from .utils import generate_password_reset_token


class UserViewSet(viewsets.ViewSet):
    """
    A ViewSet for managing user-related operations including:
    - User registration and activation
    - Login
    - Switching roles
    - Viewing own profile
    - Password reset requests and submissions
    - Token validation
    """

    def get_permissions(self):
        """
        Set permissions dynamically based on action.
        Public access allowed for registration and password reset.
        """
        if self.action == "me":
            return [IsAuthenticated(), InvestorRolePermission()]
        if self.action in [
            "create_role",
            "login",
            "register",
            "reset_password",
            "validate_reset_token",
            "reset_password_request",
        ]:
            return [AllowAny()]
        return [IsAuthenticated()]

    # TODO: remove /me route after testing
    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        logger.info(
            f"User profile request from user ID: {request.user.id if request.user.is_authenticated else 'anonymous'}"
        )
        user = request.user
        if not user.is_authenticated:
            logger.warning("Unauthenticated user attempted to access profile endpoint")
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = UserSerializer(user, context={"request": request})
        logger.debug(f"Successfully retrieved profile for user ID: {user.id}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    # TODO: only admins can create roles. remove create_role from get_permissions once implemented
    @action(detail=False, methods=["post"], url_path="create-role")
    def create_role(self, request):
        """
        Create the user's role.
        """
        logger.info(
            f"Role creation request from user ID: {request.user.id if request.user.is_authenticated else 'anonymous'}"
        )
        serializer = UserRoleSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            role = serializer.validated_data["role"]
            new_role = UserRole.objects.create(role=role)
            logger.info(
                f"Successfully created role: {new_role.role} with ID: {new_role.id}"
            )
            return Response(
                {"message": f"Role {new_role.role} created."},
                status=status.HTTP_201_CREATED,
            )

        logger.warning(f"Role creation failed with errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="switch-role")
    def switch_role(self, request):
        """
        Switch the user's role.
        """
        user = request.user
        role_id = request.data.get("role_id")
        logger.info(
            f"Role switch request from user ID: {user.id} to role ID: {role_id}"
        )

        if not role_id:
            logger.warning(
                f"Role switch failed: missing role_id for user ID: {user.id}"
            )
            return Response(
                {"detail": "Role ID is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        role = UserRole.objects.filter(id=role_id).first()
        if not role:
            logger.warning(
                f"Role switch failed: role ID {role_id} does not exist for user ID: {user.id}"
            )
            return Response(
                {"detail": "Role does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        old_role = user.role.role if user.role else "None"
        user.role = role
        user.save()
        logger.info(
            f"Successfully switched user ID: {user.id} from role '{old_role}' to '{role.role}'"
        )
        return Response(
            {"message": "Role switched successfully."}, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["post"], url_path="register")
    def register(self, request):
        """
        Register a new user.
        """
        logger.info(
            f"User registration attempt for email: {request.data.get('email', 'not provided')}"
        )
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save()

                # Login blocking until activation
                user.is_active = False
                user.save(update_fields=["is_active"])

                # Generate a token and send a letter
                token = generate_activation_token(user)
                send_activation_email(token, user.email)

                logger.info(
                    f"Successfully registered user ID: {user.id} with email: {user.email}"
                )
                # TODO: tokens
                return Response(
                    {
                        "message": "Registration successful.",
                        "user_id": user.id,
                        "email": user.email,
                    },
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                logger.error(f"Error during user registration: {str(e)}", exc_info=True)
                return Response(
                    {"detail": "Registration failed due to an internal error."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        logger.error(
            f"User registration failed with validation errors: {serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="activate")
    def activate(self, request):
        """
        Confirm email by token.
        Expects POST with JSON body: {"token": "<activation_token>"}
        """
        token = request.data.get("token")
        logger.info("Account activation attempt")

        if not token:
            logger.warning("Account activation failed: missing token")
            return Response(
                {"detail": "Token is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user, error = verify_activation_token(token)
        if not user:
            logger.warning(f"Account activation failed: {error}")
            return Response({"detail": error}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            user.is_active = True
            user.save(update_fields=["is_active"])
            logger.info(f"Successfully activated account for user ID: {user.id}")

        return Response(
            {"detail": "Account activated successfully"}, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["post"], url_path="resend-activation")
    def resend_activation(self, request):
        """
        Resend activation email to a user who has not activated their account.
        Expects POST with JSON body: {"email": "<user_email>"}
        """
        email = request.data.get("email")
        logger.info(f"Resend activation request for email: {email}")

        if not email:
            logger.warning("Resend activation failed: missing email")
            return Response(
                {"detail": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = UserProfile.objects.filter(email=email).first()
        if not user:
            logger.info(f"Resend activation: email {email} not found in database")
            # From a security perspective, the message does not reveal the existence of the email.
            return Response(
                {"detail": "If the email exists, an activation link has been sent."},
                status=status.HTTP_200_OK,
            )

        if user.is_active:
            logger.warning(
                f"Resend activation failed: account already active for email: {email}"
            )
            return Response(
                {"detail": "Account is already active."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Generate a new activation token and send the email
        try:
            token = generate_activation_token(user)
            send_activation_email(token, user.email)
            logger.info(f"Successfully resent activation email to user ID: {user.id}")
        except Exception as e:
            logger.error(
                f"Error sending activation email to user ID {user.id}: {str(e)}",
                exc_info=True,
            )

        return Response(
            {"detail": "If the email exists, an activation link has been sent."},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        logger.info(f"Login attempt for email: {email}")

        if not email or not password:
            logger.warning("Login failed: missing email or password")
            return Response(
                {"detail": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = authenticate(email=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                logger.info(
                    f"Successful login for user ID: {user.id} with email: {email}"
                )
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "username": user.username,
                        "user": {
                            "id": user.id,
                            "email": user.email,
                            "username": user.username,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "role": user.role.role if user.role else None,
                        },
                    },
                    status=status.HTTP_200_OK,
                )

            logger.warning(
                f"Failed login attempt for email: {email} - invalid credentials"
            )
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            logger.error(
                f"Error during login for email {email}: {str(e)}", exc_info=True
            )
            return Response(
                {"detail": "Login failed due to an internal error."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(detail=False, methods=["post"], url_path="validate-reset-token")
    def validate_reset_token(self, request):
        logger.info("Password reset token validation attempt")
        serializer = TokenVerificationSerializer(data=request.data)
        if serializer.is_valid():
            logger.info("Password reset token validation successful")
            return Response(
                {"valid": True, "message": "Token is valid"}, status=status.HTTP_200_OK
            )
        logger.warning(f"Password reset token validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="reset-password")
    def reset_password(self, request):
        logger.info("Password reset submission attempt")
        serializer = PasswordResetSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                logger.info("Password reset successful")
                return Response({"message": "Password reset successful"})
            except Exception as e:
                logger.error(f"Error during password reset: {str(e)}", exc_info=True)
                return Response(
                    {"detail": "Password reset failed due to an internal error."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        logger.warning(
            f"Password reset failed with validation errors: {serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="reset-password-request")
    def reset_password_request(self, request):
        logger.info("Password reset request attempt")
        serializer = PasswordResetRequestSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning(
                f"Password reset request failed with validation errors: {serializer.errors}"
            )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"]
        user = UserProfile.objects.filter(email=email).first()
        if user:
            try:
                token = generate_password_reset_token(user)
                reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token}"
                send_mail(
                    subject="Reset your password",
                    message=f"Click the link to reset your password: {reset_url}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                )
                logger.info(f"Password reset email sent to user ID: {user.id}")
            except Exception as e:
                logger.error(
                    f"Error sending password reset email to user ID {user.id}: {str(e)}",
                    exc_info=True,
                )
        else:
            logger.info(f"Password reset request for non-existent email: {email}")

        return Response(
            {"message": "If the email exist, a reset link has been send."},
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    """
    API endpoint for logging out users by blacklisting their refresh tokens.
    Requires authentication via JWT.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logger.info(f"Logout attempt for user ID: {request.user.id}")
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"Successful logout for user ID: {request.user.id}")
            return Response(
                {"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT
            )
        except (KeyError, TokenError, InvalidToken) as e:
            logger.warning(f"Logout failed for user ID {request.user.id}: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
