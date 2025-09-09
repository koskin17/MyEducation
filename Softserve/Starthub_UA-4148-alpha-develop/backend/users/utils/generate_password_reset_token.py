import hashlib
import secrets
from datetime import timedelta

from django.utils import timezone

from users.models import PasswordResetToken


def generate_password_reset_token(user):
    raw_token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    expires_at = timezone.now() + timedelta(hours=1)

    PasswordResetToken.objects.filter(user=user).delete()
    PasswordResetToken.objects.create(
        user=user, token_hash=token_hash, expires_at=expires_at
    )

    return raw_token
