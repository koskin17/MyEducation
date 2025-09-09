from django.urls import path
from .views import (
    ViewedStartupListView,
    ViewedStartupCreateView,
    ClearViewedStartupsView,
)

urlpatterns = [
    path("startups/viewed", ViewedStartupListView.as_view(), name="viewed-startups"),
    path(
        "startups/view/<int:startup_id>",
        ViewedStartupCreateView.as_view(),
        name="view-startup",
    ),
    path(
        "startups/viewed/clear",
        ClearViewedStartupsView.as_view(),
        name="clear-viewed-startups",
    ),
]
