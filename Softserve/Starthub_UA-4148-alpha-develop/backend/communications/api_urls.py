from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import RoomViewSet, MessageViewSet

router = DefaultRouter()
router.register(r"rooms", RoomViewSet, basename="room")
router.register(r"messages", MessageViewSet, basename="message")

urlpatterns = [
    path("", include(router.urls)),
]
