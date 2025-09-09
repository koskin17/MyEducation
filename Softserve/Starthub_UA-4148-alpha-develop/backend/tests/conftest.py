import pytest
from django.contrib.auth import get_user_model
from profiles.models import StartupProfile
from users.models import UserRole

User = get_user_model()


@pytest.fixture
def startup_role(db):
    role, _ = UserRole.objects.get_or_create(role="startup")
    return role


@pytest.fixture
def create_investor(db):
    role, _ = UserRole.objects.get_or_create(role="investor")

    def _create(email="investor@example.com", username="investor"):
        return User.objects.create_user(
            email=email, username=username, password="testpass123", role=role
        )

    return _create


@pytest.fixture
def create_startup(db):
    def _create(user, company_name="Test Startup"):
        return StartupProfile.objects.create(
            user=user,
            company_name=company_name,
            description="Some description",
            website="http://example.com",
        )

    return _create
