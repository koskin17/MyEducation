from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, SavedProjectsList

router = DefaultRouter()
router.register(r"", ProjectViewSet, basename="project")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "investor/saved-projects/",
        SavedProjectsList.as_view(),
        name="investor-saved-projects",
    ),
]
