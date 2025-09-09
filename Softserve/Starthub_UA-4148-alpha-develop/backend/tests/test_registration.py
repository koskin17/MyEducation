import pytest
from django.urls import reverse
from rest_framework.test import APIClient

NEW_USER = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "StrongPassw0rd!",
    "confirm_password": "StrongPassw0rd!",
    "company_name": "Test",
    "representative_type": "investor",
    "first_name": "Test",
    "last_name": "User",
    "role": None,
}


@pytest.mark.django_db
class TestUserRegistration:
    """Test cases for the user registration endpoint."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.url = reverse("user-register")

    def test_register_success(self):
        response = self.client.post(self.url, data=NEW_USER, format="json")
        assert response.status_code == 201
        assert response.data["email"] == NEW_USER["email"]
        assert "user_id" in response.data
        assert response.data["message"] == "Registration successful."

    def test_register_password_mismatch(self):
        data = NEW_USER
        data["confirm_password"] = "WrongPassw0rd"
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 400
        assert "password" in response.data
        assert response.data["password"][0] == "The passwords do not match."

    def test_register_existing_email(self):
        from users.models import UserProfile

        UserProfile.objects.create_user(
            username="existinguser",
            email="testuser@example.com",
            password="SomePass123!",
        )
        response = self.client.post(self.url, data=NEW_USER, format="json")

        assert response.status_code == 400
        assert "email" in response.data
        assert len(response.data["email"]) > 0
        assert any(
            "already in use" in str(msg).lower() or "exists" in str(msg).lower()
            for msg in response.data["email"]
        )
