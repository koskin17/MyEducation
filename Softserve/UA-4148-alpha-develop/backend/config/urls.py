from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

SchemaView = get_schema_view(
    openapi.Info(
        title="StartHub API",
        default_version="v1",
        description="API documentation for StartHub platform",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="contact@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

token_urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

api_urlpatterns = [
    path("token/", include(token_urlpatterns)),
    path("", include("users.urls")),
    path("chat/", include("communications.api_urls")),
    path("projects/", include("projects.urls")),
    path("profiles/", include("profiles.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    path(
        "swagger<format>/", SchemaView.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", SchemaView.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("chat/", include("communications.urls")),
    path("", include("projects.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
