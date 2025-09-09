from django.contrib.auth.backends import ModelBackend

from users.models import UserProfile


class EmailBackend(ModelBackend):
    """Authenticate users using their email and password instead of username."""

    def authenticate(
        self, request, email=None, password=None, **kwargs
    ):  # pylint: disable=W0237
        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
