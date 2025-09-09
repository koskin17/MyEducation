import bleach
from django.utils import timezone

from communications.mongo_models import Message


def save_message(room, user, text):
    sanitized_text = bleach.clean(text, tags=[], attributes={}, strip=True)

    message = Message(
        room=room,
        sender_id=str(user.id),
        sender_first_name=user.first_name,
        sender_last_name=user.last_name,
        text=sanitized_text,
        timestamp=timezone.now(),
        is_read=False,
    )
    message.save()
    room.updated_at = timezone.now()
    room.save()
    return message
