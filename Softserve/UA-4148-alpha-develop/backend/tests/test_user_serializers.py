import hashlib
from datetime import timedelta
import datetime
import pytest
from django.utils import timezone

from users.models import PasswordResetToken, UserProfile
from users.serializers import (
    PasswordResetRequestSerializer,
    PasswordResetSubmissionSerializer,
    TokenVerificationSerializer,
    UserRegistrationSerializer,
)
from users.utils.generate_password_reset_token import generate_password_reset_token
from users.utils.verify_reset_token import verify_reset_token


@pytest.mark.django_db
def test_user_registration_serializer_valid_and_invalid():
    # Спочатку створюємо одного користувача
    UserProfile.objects.filter(username="existinguser").delete()
    UserProfile.objects.create_user(
        username="existinguser", email="existing@example.com", password="TestPass123!"
    )

    # Тепер пробуємо зареєструвати користувача з таким же username через serializer
    duplicate_username_data = {
        "username": "existinguser",
        "email": "unique@example.com",
        "password": "ComplexPass123!",
        "confirm_password": "ComplexPass123!",
        "company_name": "Test",
        "representative_type": "investor",
    }
    serializer = UserRegistrationSerializer(data=duplicate_username_data)
    assert not serializer.is_valid()
    assert "username" in serializer.errors


@pytest.mark.django_db
def test_password_reset_request_serializer():
    serializer = PasswordResetRequestSerializer(data={"email": "test@example.com"})
    assert serializer.is_valid()


@pytest.mark.django_db
def test_token_verification_serializer_valid_and_invalid():
    user = UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="pass123"
    )
    from unittest.mock import patch

    raw_token = "validtoken"
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    PasswordResetToken.objects.create(
        user=user,
        token_hash=token_hash,
        expires_at=timezone.now() + datetime.timedelta(hours=1),
    )

    with patch(
        "users.serializers.verify_reset_token", return_value=(True, "Token is valid")
    ):
        data = {"token": raw_token}
        serializer = TokenVerificationSerializer(data=data)
        assert serializer.is_valid()

    data = {"token": "token"}
    serializer = TokenVerificationSerializer(data=data)
    assert not serializer.is_valid()

    with patch(
        "users.serializers.verify_reset_token", return_value=(False, "Invalid token")
    ):
        data = {"token": "badtoken"}
        serializer = TokenVerificationSerializer(data=data)
        assert not serializer.is_valid()


@pytest.mark.django_db
def test_password_reset_submission_serializer_valid_and_invalid():
    user = UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="pass123"
    )

    raw_token = "validtoken"
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    PasswordResetToken.objects.create(
        user=user,
        token_hash=token_hash,
        expires_at=timezone.now() + datetime.timedelta(hours=1),
    )

    from unittest.mock import patch

    valid_data = {
        "token": raw_token,
        "password": "ComplexPass123!",
        "confirm_password": "ComplexPass123!",
    }

    with patch(
        "users.serializers.verify_reset_token", return_value=(True, "Token is valid")
    ):
        serializer = PasswordResetSubmissionSerializer(data=valid_data)
        assert serializer.is_valid(), serializer.errors
        serializer.save()
        user.refresh_from_db()
        assert user.check_password(valid_data["password"])

    invalid_data = valid_data.copy()
    invalid_data["confirm_password"] = "Mismatch"
    serializer = PasswordResetSubmissionSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert "Passwords do not match." in str(serializer.errors)

    invalid_data = valid_data.copy()
    invalid_data["token"] = "invalidtoken"
    with patch(
        "users.serializers.verify_reset_token", return_value=(True, "Token is valid")
    ):
        serializer = PasswordResetSubmissionSerializer(data=invalid_data)
        assert not serializer.is_valid()

    with patch(
        "users.serializers.verify_reset_token", return_value=(False, "Invalid token")
    ):
        serializer = PasswordResetSubmissionSerializer(data=valid_data)
        assert not serializer.is_valid()

    weak_password_data = valid_data.copy()
    weak_password_data["password"] = "123"
    weak_password_data["confirm_password"] = "123"
    with patch(
        "users.serializers.verify_reset_token", return_value=(True, "Token is valid")
    ):
        serializer = PasswordResetSubmissionSerializer(data=weak_password_data)
        assert not serializer.is_valid()
        errors_str = str(serializer.errors)
        assert "password" in errors_str or "non_field_errors" in errors_str


@pytest.mark.django_db
def test_verify_reset_token_returns_true_for_valid_token():
    user = UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="pass123"
    )
    raw_token = generate_password_reset_token(user)

    is_valid, msg = verify_reset_token(user, raw_token)

    assert is_valid is True
    assert msg == "Token is valid"

    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    assert not PasswordResetToken.objects.filter(
        user=user, token_hash=token_hash
    ).exists()


@pytest.mark.django_db
def test_verify_reset_token_returns_false_for_invalid_token():
    user = UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="pass123"
    )
    fake_token = "invalidtokenstring"

    is_valid, msg = verify_reset_token(user, fake_token)

    assert is_valid is False
    assert msg == "Invalid token"


@pytest.mark.django_db
def test_verify_reset_token_returns_false_and_deletes_expired_token():
    user = UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="pass123"
    )
    raw_token = generate_password_reset_token(user)

    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    token_obj = PasswordResetToken.objects.get(user=user, token_hash=token_hash)
    token_obj.expires_at = timezone.now() - timedelta(minutes=1)
    token_obj.save()

    is_valid, msg = verify_reset_token(user, raw_token)

    assert is_valid is False
    assert msg == "Token expired"
    assert not PasswordResetToken.objects.filter(
        user=user, token_hash=token_hash
    ).exists()
