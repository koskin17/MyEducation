import bleach
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .mongo_models import Room
from .utils.generate_room_name import generate_room_name
from .utils.save_message import save_message

User = get_user_model()


class ParticipantSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    first_name = serializers.CharField(allow_blank=True, required=False)
    last_name = serializers.CharField(allow_blank=True, required=False)


class RoomSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    participants = ParticipantSerializer(many=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(read_only=True)


class MessageSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    room_id = serializers.CharField(write_only=True, required=False)
    other_user_id = serializers.CharField(write_only=True, required=False)
    sender_id = serializers.CharField(read_only=True)
    sender_first_name = serializers.CharField(read_only=True)
    sender_last_name = serializers.CharField(read_only=True)
    text = serializers.CharField()
    timestamp = serializers.DateTimeField(read_only=True)
    is_read = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        room_id = attrs.get("room_id")
        user = self.context["request"].user
        other_user_id = attrs.get("other_user_id")

        if not (other_user_id or room_id):
            raise serializers.ValidationError(
                "Either room_id or other_user_id is required."
            )

        if room_id:
            try:
                room = Room.objects.get(id=room_id)
            except Room.DoesNotExist:
                raise serializers.ValidationError({"room_id": "Room not found."})
            if not any(str(p["id"]) == str(user.id) for p in room.participants):
                raise serializers.ValidationError(
                    "You are not a participant of this room."
                )
            attrs["room"] = room

        else:
            if str(other_user_id) == str(user.id):
                raise serializers.ValidationError("Cannot message yourself.")

            try:
                other_user = User.objects.get(id=other_user_id)
            except User.DoesNotExist:
                raise serializers.ValidationError(
                    {"other_user_id": "Receiver not found."}
                )

            sender_role = getattr(user.role, "role", None)
            receiver_role = getattr(other_user.role, "role", None)

            if sender_role not in {"investor", "startup"} or receiver_role not in {
                "investor",
                "startup",
            }:
                raise serializers.ValidationError(
                    "Messaging allowed only between investor and startup."
                )
            if sender_role == receiver_role:
                raise serializers.ValidationError(
                    "Messaging allowed only between investor and startup."
                )

            try:
                room_name = generate_room_name(user, other_user)
            except ValueError as e:
                raise serializers.ValidationError(str(e))

            room = Room.objects(name=room_name).first()
            if not room:
                if sender_role != "investor":
                    raise serializers.ValidationError(
                        "Only investors can start a new conversation."
                    )
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

            attrs["room"] = room

        text = attrs.get("text", "").strip()
        if not text:
            raise serializers.ValidationError({"text": "Message cannot be empty"})
        if len(text) > 1000:
            raise serializers.ValidationError(
                {"text": "Message is too long (max 1000 chars)"}
            )
        sanitized_text = bleach.clean(text)
        attrs["text"] = sanitized_text

        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        room = validated_data["room"]
        text = validated_data["text"]

        return save_message(room, user, text)
