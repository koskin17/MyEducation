from django.core.exceptions import PermissionDenied, ValidationError

from communications.mongo_models import Room
from .generate_room_name import generate_room_name

from django.contrib.auth import get_user_model


User = get_user_model()


def get_or_create_room(user, room_id=None, other_user_id=None):
    if not user or not getattr(user, "is_authenticated", False):
        raise PermissionDenied("User must be authenticated.")

    if not (room_id or other_user_id):
        raise ValidationError("Either room_id or other_user_id is required.")

    if room_id:
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise ValidationError({"room_id": "Room not found."})
        if not any(str(p["id"]) == str(user.id) for p in room.participants):
            raise ValidationError("You are not a participant of this room.")
        return room

    if str(other_user_id) == str(user.id):
        raise ValidationError("Cannot message yourself.")

    try:
        other_user = User.objects.get(id=other_user_id)
    except User.DoesNotExist:
        raise ValidationError({"other_user_id": "Receiver not found."})

    sender_role = getattr(user.role, "role", None)
    receiver_role = getattr(other_user.role, "role", None)

    if sender_role not in {"investor", "startup"} or receiver_role not in {
        "investor",
        "startup",
    }:
        raise PermissionDenied("Messaging allowed only between investor and startup.")
    if sender_role == receiver_role:
        raise PermissionDenied("Messaging allowed only between investor and startup.")

    try:
        room_name = generate_room_name(user, other_user)
    except ValueError as e:
        raise ValidationError(str(e))

    room = Room.objects(name=room_name).first()
    if room:
        return room

    if sender_role != "investor":
        raise PermissionDenied("Only investors can start a new conversation.")

    participants = [
        {
            "id": str(user.id),
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
        {
            "id": str(other_user.id),
            "username": other_user.username,
            "first_name": other_user.first_name,
            "last_name": other_user.last_name,
        },
    ]
    room = Room(name=room_name, participants=participants)
    room.save()
    return room
