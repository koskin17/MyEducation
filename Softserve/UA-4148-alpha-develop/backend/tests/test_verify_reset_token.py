import hashlib
from datetime import timedelta

import pytest
from django.utils import timezone

from users.models import PasswordResetToken, UserProfile
from users.utils.generate_password_reset_token import generate_password_reset_token
from users.utils.verify_reset_token import verify_reset_token


@pytest.fixture
def user_instance(db):
    return UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="pass123"
    )


@pytest.mark.django_db
def test_verify_reset_token_returns_true_for_valid_token(user_instance):
    raw_token = generate_password_reset_token(user_instance)

    is_valid, msg = verify_reset_token(user_instance, raw_token)

    assert is_valid is True
    assert msg == "Token is valid"

    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    assert not PasswordResetToken.objects.filter(
        user=user_instance, token_hash=token_hash
    ).exists()


@pytest.mark.django_db
def test_verify_reset_token_returns_false_for_invalid_token(user_instance):
    fake_token = "invalidtokenstring"

    is_valid, msg = verify_reset_token(user_instance, fake_token)

    assert is_valid is False
    assert msg == "Invalid token"


@pytest.mark.django_db
def test_verify_reset_token_returns_false_and_deletes_expired_token(user_instance):
    raw_token = generate_password_reset_token(user_instance)

    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    token_obj = PasswordResetToken.objects.get(
        user=user_instance, token_hash=token_hash
    )
    token_obj.expires_at = timezone.now() - timedelta(minutes=1)
    token_obj.save()

    is_valid, msg = verify_reset_token(user_instance, raw_token)

    assert is_valid is False
    assert msg == "Token expired"
    assert not PasswordResetToken.objects.filter(
        user=user_instance, token_hash=token_hash
    ).exists()
