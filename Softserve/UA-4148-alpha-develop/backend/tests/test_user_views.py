import pytest
from django.core import mail
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import UserProfile
from users.utils import generate_password_reset_token


@pytest.mark.django_db
def test_register_success():
    client = APIClient()
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "ComplexPass123!",
        "confirm_password": "ComplexPass123!",
        "company_name": "Test",
        "representative_type": "investor",
        "first_name": "Test",
        "last_name": "User",
        "role": "",
    }
    url = reverse("user-register")
    response = client.post(url, data)
    assert response.status_code == 201
    assert UserProfile.objects.filter(email="test@example.com").exists()


@pytest.mark.django_db
def test_login_success():
    client = APIClient()
    UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="TestPass123!"
    )

    url = reverse("user-login")
    response = client.post(
        url, {"email": "test@example.com", "password": "TestPass123!"}
    )
    assert response.status_code == 200
    assert "access" in response.data


@pytest.mark.django_db
def test_login_missing_fields():
    client = APIClient()

    url = reverse("user-login")
    response = client.post(url, {})
    assert response.status_code == 400
    assert "detail" in response.data


@pytest.mark.django_db
def test_validate_reset_token_valid():
    client = APIClient()
    user = UserProfile.objects.create_user(
        username="resetuser", email="reset@example.com", password="123passWord!"
    )
    token = generate_password_reset_token(user)

    url = reverse("user-validate-reset-token")
    response = client.post(url, {"email": user.email, "token": token}, format="json")
    assert response.status_code == 200
    assert response.data["valid"] is True


@pytest.mark.django_db
def test_validate_reset_token_invalid():
    client = APIClient()

    url = reverse("user-validate-reset-token")
    response = client.post(
        url, {"email": "noone@example.com", "token": "invalidtoken"}, format="json"
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_password_reset_sends_email(settings):
    client = APIClient()
    UserProfile.objects.create_user(
        username="emailuser", email="email@example.com", password="pass"
    )

    url = reverse("user-reset-password-request")
    response = client.post(url, {"email": "email@example.com"})
    assert response.status_code == 200
    assert len(mail.outbox) == 1
    assert "reset" in mail.outbox[0].subject.lower()


@pytest.mark.django_db
def test_password_reset_submission_valid():
    client = APIClient()
    user = UserProfile.objects.create_user(
        username="reseter", email="reseter@example.com", password="123Pass!!"
    )
    token = generate_password_reset_token(user)

    url = reverse("user-reset-password")
    response = client.post(
        url,
        {
            "email": user.email,
            "token": token,
            "password": "NewStrongPass1!",
            "confirm_password": "NewStrongPass1!",
        },
    )

    assert response.status_code == 200
    user.refresh_from_db()
    assert user.check_password("NewStrongPass1!")


@pytest.mark.django_db
def test_password_reset_submission_mismatch_passwords():
    client = APIClient()
    user = UserProfile.objects.create_user(
        username="reseter2", email="reseter2@example.com", password="123Pass!!"
    )
    token = generate_password_reset_token(user)

    url = reverse("user-reset-password")
    response = client.post(
        url,
        {
            "email": user.email,
            "token": token,
            "password": "Password1!",
            "confirm_password": "DoesNotMatch",
        },
    )

    assert response.status_code == 400
    assert "passwords do not match" in str(response.data).lower()
