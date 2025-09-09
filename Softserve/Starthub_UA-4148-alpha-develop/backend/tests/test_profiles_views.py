import pytest
from rest_framework.test import APIClient
from profiles.models import ViewedStartup
from unittest.mock import patch, AsyncMock
from django.urls import reverse
from projects.models import StartupProject, ProjectRevision
from profiles.models import StartupProfile
from users.models import UserProfile, UserRole


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def clear_viewed_startups():
    ViewedStartup.objects.all().delete()


@pytest.mark.django_db
def test_startup_view_logged(api_client, create_investor, create_startup):
    investor = create_investor(email="investor1@test.com", username="investor1")
    startup = create_startup(user=investor, company_name="Startup 1")

    api_client.force_authenticate(user=investor)

    url = f"/api/profiles/startups/view/{startup.id}"
    response = api_client.post(url)

    assert response.status_code == 201
    assert "viewed successfully" in response.data["message"]


@pytest.mark.django_db
def test_list_recently_viewed_startups(api_client, create_investor, create_startup):
    investor = create_investor(email="investor2@test.com", username="investor2")
    startup = create_startup(user=investor, company_name="Startup 2")

    api_client.force_authenticate(user=investor)
    api_client.post(f"/api/profiles/startups/view/{startup.id}")

    response = api_client.get("/api/profiles/startups/viewed")
    results = response.data["results"]
    assert response.status_code == 200
    assert len(results) == 1
    assert results[0]["company_name"] == startup.company_name


@pytest.mark.django_db
def test_clear_viewed_startups(api_client, create_investor, create_startup):
    investor = create_investor(email="investor3@test.com", username="investor3")
    startup = create_startup(user=investor, company_name="Startup 3")

    api_client.force_authenticate(user=investor)
    api_client.post(f"/api/profiles/startups/view/{startup.id}")

    response = api_client.delete("/api/profiles/startups/viewed/clear")
    assert response.status_code == 200
    assert "cleared" in response.data["message"]

    response = api_client.get("/api/profiles/startups/viewed")
    results = response.data["results"]
    assert len(results) == 0


@pytest.mark.django_db
def test_permissions_only_investors(
    api_client, create_startup, create_investor, startup_role
):
    user = create_investor(email="startup@test.com", username="startup_user")
    user.role = startup_role
    user.save()

    startup = create_startup(user=user, company_name="Startup 1")

    api_client.force_authenticate(user=user)

    url = f"/api/profiles/startups/view/{startup.id}"
    response = api_client.post(url)

    assert response.status_code == 403


@pytest.fixture
def investor_user(db):
    role, _ = UserRole.objects.get_or_create(role="investor")
    return UserProfile.objects.create_user(
        email="investor@example.com", username="investor", password="pass123", role=role
    )


@pytest.fixture
def startup_project(db, investor_user):
    startup = StartupProfile.objects.create(
        user=investor_user, company_name="Test Startup"
    )
    return StartupProject.objects.create(
        subject="Old Project", idea="Old Idea", startup=startup
    )


@pytest.mark.django_db
def test_update_project_creates_revision(api_client, startup_project, investor_user):
    api_client.force_authenticate(user=investor_user)
    url = reverse("project-update-project", args=[startup_project.id])

    data = {"subject": "New Project", "idea": "New Idea"}

    with patch("projects.views.get_channel_layer") as mock_layer:
        mock_channel = mock_layer.return_value
        mock_channel.group_send = AsyncMock()

        response = api_client.post(url, data)

        assert response.status_code == 200
        assert response.data["project"]["subject"] == "New Project"

        revision = ProjectRevision.objects.get(project=startup_project)
        assert revision.changes["subject"]["old"] == "Old Project"
        assert revision.changes["subject"]["new"] == "New Project"

        mock_channel.group_send.assert_called_once()
