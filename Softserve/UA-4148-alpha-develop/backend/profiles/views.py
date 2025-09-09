import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import StartupProfile, ViewedStartup
from .serializers import ViewedStartupSerializer, StartupProfileSerializer
from .permissions import IsInvestor
from django.utils import timezone
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination

# Get logger for this module
logger = logging.getLogger(__name__)


class ViewedStartupPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50


class ViewedStartupListView(generics.ListAPIView):
    serializer_class = ViewedStartupSerializer
    permission_classes = [IsInvestor]
    pagination_class = ViewedStartupPagination

    def get_queryset(self):
        logger.info(f"ViewedStartup list request from user ID: {self.request.user.id}")
        return ViewedStartup.objects.filter(user=self.request.user).order_by(
            "-viewed_at"
        )


class ViewedStartupCreateView(APIView):
    permission_classes = [IsInvestor]

    def post(self, request, startup_id):
        logger.info(
            f"ViewedStartup create request from user ID: {request.user.id} for startup ID: {startup_id}"
        )
        try:
            startup = get_object_or_404(StartupProfile, id=startup_id)

            obj, created = ViewedStartup.objects.get_or_create(
                user=request.user,
                startup=startup,
            )
            if not created:
                obj.viewed_at = timezone.now()
                obj.save()

            logger.info(
                f"Successfully recorded view for startup '{startup.company_name}' by user ID: {request.user.id}"
            )
            return Response(
                {"message": f"Startup '{startup.company_name}' viewed successfully."},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            logger.error(
                f"Error creating ViewedStartup for user ID {request.user.id} and startup ID {startup_id}: {str(e)}",
                exc_info=True,
            )
            return Response(
                {"detail": "Failed to record startup view."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ClearViewedStartupsView(APIView):
    permission_classes = [IsInvestor]

    def delete(self, request):
        logger.info(f"Clear viewed startups request from user ID: {request.user.id}")
        try:
            ViewedStartup.objects.filter(user=request.user).delete()
            logger.info(
                f"Successfully cleared viewed startups history for user ID: {request.user.id}"
            )
            return Response(
                {"message": "Viewed startups history cleared successfully."}
            )
        except Exception as e:
            logger.error(
                f"Error clearing viewed startups for user ID {request.user.id}: {str(e)}",
                exc_info=True,
            )
            return Response(
                {"detail": "Failed to clear viewed startups history."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class StartupViewSet(ReadOnlyModelViewSet):
    queryset = StartupProfile.objects.all()
    serializer_class = StartupProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        logger.info(
            f"Startup retrieve request from user ID: {request.user.id} for startup ID: {kwargs.get('pk')}"
        )
        try:
            response = super().retrieve(request, *args, **kwargs)

            if request.user.is_authenticated and request.user.is_investor():
                startup = self.get_object()
                obj, created = ViewedStartup.objects.get_or_create(
                    user=request.user, startup=startup
                )
                if not created:
                    obj.viewed_at = timezone.now()
                    obj.save()
                logger.info(
                    f"Successfully recorded view for startup '{startup.company_name}' by investor user ID: {request.user.id}"
                )

            return response
        except Exception as e:
            logger.error(
                f"Error retrieving startup for user ID {request.user.id}: {str(e)}",
                exc_info=True,
            )
            return Response(
                {"detail": "Failed to retrieve startup."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
