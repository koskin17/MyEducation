import hashlib

from users.models import PasswordResetToken


def verify_reset_token(user, raw_token):
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()

    try:
        reset_token = PasswordResetToken.objects.get(user=user, token_hash=token_hash)
    except PasswordResetToken.DoesNotExist:
        return False, "Invalid token"

    if not reset_token.is_valid():
        reset_token.delete()
        return False, "Token expired"

    reset_token.delete()
    return True, "Token is valid"
