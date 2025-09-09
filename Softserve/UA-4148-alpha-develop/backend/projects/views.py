import logging
from rest_framework import status, viewsets, generics, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.db.models import F
from django.db import transaction

from django_filters.rest_framework import DjangoFilterBackend

from profiles.models import InvestorProfile
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .serializers import ProjectSerializer, SubscriptionSerializer
from .models import StartupProject, Subscription, ProjectRevision
from .permissions import IsInvestor, IsStartup

# Get logger for this module
logger = logging.getLogger(__name__)


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, retrieving, and subscribing to projects."""

    permission_classes = [IsAuthenticated, IsInvestor]
    queryset = StartupProject.objects.all()
    serializer_class = ProjectSerializer

    # Filters for base List
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["subject", "idea", "description", "startup__company_name"]
    ordering_fields = ["created_at", "views_count", "funding_goal"]

    def get_permissions(self):
        if self.action in ["create"]:
            permission_classes = [IsAuthenticated, IsStartup]
        elif self.action in ["list", "retrieve", "save", "unsave"]:
            permission_classes = [IsAuthenticated, IsInvestor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Creation a project is automatically link it to a startup"""
        startup_profile = getattr(self.request.user, "startupprofile", None)
        if not startup_profile:
            raise Exception("Startup profile not found for this user.")
        serializer.save(startup=startup_profile)

    def list(self, request, *args, **kwargs):
        """Viewing projects by investors"""
        logger.info(f"Project list request from user ID: {request.user.id}")
        try:
            queryset = self.get_queryset().order_by("-created_at")
            serializer = self.get_serializer(queryset, many=True)
            logger.debug(
                f"Successfully retrieved {len(serializer.data)} projects for user ID: {request.user.id}"
            )
            return Response(serializer.data)
        except Exception as e:
            logger.error(
                f"Error retrieving project list for user ID {request.user.id}: {str(e)}",
                exc_info=True,
            )
            return Response(
                {"detail": "Failed to retrieve projects."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def retrieve(self, request, *args, **kwargs):
        logger.info(
            f"Project retrieve request from user ID: {request.user.id} for project ID: {kwargs.get('pk')}"
        )

        try:
            project = self.get_object()

            # View counter update
            StartupProject.objects.filter(pk=project.pk).update(
                views_count=F("views_count") + 1
            )
            project.refresh_from_db(fields=["views_count"])

            serializer = self.get_serializer(project)
            logger.debug(
                f"Successfully retrieved project ID: {kwargs.get('pk')} for user ID: {request.user.id}"
            )
            return Response(serializer.data)
        except Exception as e:
            logger.error(
                f"Error retrieving project ID {kwargs.get('pk')} for user ID {request.user.id}: {str(e)}",
                exc_info=True,
            )
            return Response(
                {"detail": "Failed to retrieve project."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    # Follow for saving projects by investor
    @action(detail=True, methods=["post"], url_path="save")
    def save(self, request, pk=None):
        """
        POST  /api/startups/{pk}/save/
        Allow an authenticated investor to follow (save) a startup project.
        """

        investor_profile = getattr(request.user, "investorprofile", None)
        if not investor_profile:
            return Response(
                {"error": "Investor profile not found for this user."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        project = self.get_object()

        # Prevent duplicates
        if investor_profile.saved_projects.filter(pk=project.pk).exists():
            serializer = ProjectSerializer(project)
            return Response(
                {"message": "Project is already saved.", "project": serializer.data},
                status=status.HTTP_200_OK,
            )

        # Atomic transaction to ensure database integrity
        with transaction.atomic():
            investor_profile.saved_projects.add(project)

        serializer = ProjectSerializer(project)

        return Response(
            {
                "message": f"Project {project.id} has been saved to your profile.",
                "project": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    # Unfollow / delete to remove a project from saved
    @action(detail=True, methods=["post", "delete"], url_path="unsave")
    def unsave(self, request, pk=None):
        """
        Allow an authenticated investor to unfollow (remove) a startup project.
        supports POST /api/projects/{pk}/unsave/ and DELETE /api/projects/{pk}/unsave/
        """

        investor_profile = getattr(request.user, "investorprofile", None)
        if not investor_profile:
            return Response(
                {"error": "Investor profile not found for this user."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        project = self.get_object()

        # Atomic transaction to ensure database integrity
        with transaction.atomic():
            investor_profile.saved_projects.remove(project)

        serializer = ProjectSerializer(project)

        if request.method == "DELETE":
            return Response(
                {
                    "message": f"Project {project.id} has been deleted from your saved list.",
                    "project": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": f"Project {project.id} has been removed from your saved list.",
                "project": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"])
    def subscribe(self, request, pk=None):
        logger.info(
            f"Project subscription request from user ID: {request.user.id} for project ID: {pk}"
        )
        try:
            project = self.get_object()
        except StartupProject.DoesNotExist:
            logger.warning(
                f"Project subscription failed: project ID {pk} not found for user ID: {request.user.id}"
            )
            return Response(
                {"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            share = serializer.validated_data["share"]

            if project.funding_goal is None:
                logger.warning(
                    f"Project subscription failed: project ID {pk} has no funding goal for user ID: {request.user.id}"
                )
                return Response(
                    {"error": "Project has no funding goal set."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if project.remaining_funding() < share:
                logger.warning(
                    f"Project subscription failed: funding goal exceeded for project ID {pk} by user ID: {request.user.id}"
                )
                return Response(
                    {"error": "Funding goal exceeded"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            subscription = serializer.save(
                investor=request.user.investorprofile, project=project
            )
            logger.info(
                f"Successfully subscribed user ID: {request.user.id} to project ID: {pk}"
            )
            return Response(
                SubscriptionSerializer(subscription).data,
                status=status.HTTP_201_CREATED,
            )

        logger.error(
            f"Project subscription failed with validation errors for user ID {request.user.id} and project ID {pk}: {serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"])
    def update_project(self, request, pk=None):
        logger.info(
            f"Project update request from user ID: {request.user.id} for project ID: {pk}"
        )
        try:
            project = StartupProject.objects.get(pk=pk, startup__user=request.user)
        except StartupProject.DoesNotExist:
            logger.warning(
                f"Project update failed: project ID {pk} not found or access denied for user ID: {request.user.id}"
            )
            return Response(
                {"detail": "Project not found or access denied."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            old_data = ProjectSerializer(project).data
            serializer.save()
            new_data = serializer.data

            changes = {
                field: {"old": old_data[field], "new": new_data[field]}
                for field in new_data
                if old_data[field] != new_data[field]
            }

            if changes:
                ProjectRevision.objects.create(
                    project=project, updated_by=request.user, changes=changes
                )
                logger.info(
                    f"Successfully updated project ID: {pk} with changes: {changes} by user ID: {request.user.id}"
                )

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"startup_{project.startup.id}",
                {"type": "project.update", "project": new_data},
            )

            return Response(
                {"message": "Project updated successfully", "project": new_data},
                status=status.HTTP_200_OK,
            )

        logger.error(
            f"Project update failed with validation errors for user ID {request.user.id} and project ID {pk}: {serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavedProjectsList(generics.ListAPIView):
    """
    GET /api/investor/saved-projects/
    Forms a list of projects that the current investor has saved.
    - search: GET /api/investor/saved-projects/?search=AI;
    - ordering: GET /api/investor/saved-projects/?ordering=funding_goal.

    Requires authentication and investor role.
    Response: JSON list of saved projects.
    """

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsInvestor]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["subject", "idea", "description", "startup__company_name"]
    ordering_fields = ["created_at", "views_count", "funding_goal"]
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user
        investor_profile = getattr(user, "investorprofile", None)

        if not investor_profile:
            raise PermissionDenied("Investor profile not found for this user.")

        if not getattr(investor_profile, "is_active", True):
            raise PermissionDenied("Account of user is not active.")

        return investor_profile.saved_projects.all()
