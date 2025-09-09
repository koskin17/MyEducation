import hashlib

import pytest
from django.utils import timezone

from users.models import PasswordResetToken, UserProfile
from users.utils.generate_password_reset_token import generate_password_reset_token


@pytest.mark.django_db
def test_generate_password_reset_token_creates_token_and_db_entry():
    user = UserProfile.objects.create_user(
        username="testuser", email="test@example.com", password="pass123"
    )

    raw_token = generate_password_reset_token(user)

    assert isinstance(raw_token, str)
    assert len(raw_token) > 0

    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    token_obj = PasswordResetToken.objects.filter(
        user=user, token_hash=token_hash
    ).first()
    assert token_obj is not None
    assert token_obj.expires_at > timezone.now()
