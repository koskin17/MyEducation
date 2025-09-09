import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import UserProfile, UserRole


@pytest.mark.django_db
class TestUserLogin:
    """
    Test suite for the user login API endpoint.

    Uses Django REST Framework's APIClient to test:
        - Successful login with correct credentials.
        - Login attempts with missing email or password.
        - Login attempts with incorrect password.
        - Login attempts for a nonexistent user.
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.role = UserRole.objects.create(role="tester")
        self.user = UserProfile.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="TestPass123!",
            role=self.role,
            first_name="Test",
            last_name="User",
        )
        self.url = reverse("user-login")

    def test_login_success(self):
        data = {"email": "testuser@example.com", "password": "TestPass123!"}
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data
        assert response.data["username"] == "testuser"
        assert response.data["user"]["email"] == "testuser@example.com"
        assert response.data["user"]["role"] == "tester"

    def test_login_missing_email_or_password(self):
        response = self.client.post(
            self.url, {"password": "TestPass123!"}, format="json"
        )
        assert response.status_code == 400
        assert response.data["detail"] == "Email and password are required."

        response = self.client.post(
            self.url, {"email": "testuser@example.com"}, format="json"
        )
        assert response.status_code == 400
        assert response.data["detail"] == "Email and password are required."

    def test_login_wrong_password(self):
        data = {"email": "testuser@example.com", "password": "WrongPassword"}
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 401
        assert response.data["detail"] == "Invalid credentials"

    def test_login_nonexistent_user(self):
        data = {"email": "nonexistent@example.com", "password": "SomePassword"}
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 401
        assert response.data["detail"] == "Invalid credentials"
