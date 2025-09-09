from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .mongo_models import Room, Message
from .permissions import IsRoomParticipant
from .serializers import RoomSerializer, MessageSerializer

User = get_user_model()


class RoomViewSet(viewsets.ModelViewSet):
    """
    Conversations (Rooms)
    """

    serializer_class = RoomSerializer

    def get_permissions(self):
        """
        Only authenticated users can access room endpoints.
        For actions that involve a specific room (retrieve, messages, mark_as_read),
        the user must also be a participant.
        """
        if self.action in ["retrieve", "messages", "mark_as_read"]:
            return [IsAuthenticated(), IsRoomParticipant()]
        return [IsAuthenticated()]

    def get_queryset(self):
        """
        Filters rooms where the current user is a participant.
        """
        return Room.objects(participants__id=str(self.request.user.id)).order_by(
            "-updated_at"
        )

    def list(self, request, *args, **kwargs):
        """
        Returns a list of rooms the current user participates in.
        """
        rooms = self.get_queryset()
        serializer = self.get_serializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Retrieve details of a specific room by ID (e.g., participants, timestamps).
        """
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "room not found"}, status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, room)
        serializer = self.get_serializer(room)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="messages")
    def messages(self, request, pk=None):
        """
        Retrieve message history for a specific room.
        Supports `?limit=` query param (default: 50).
        """
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "room not found"}, status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, room)

        try:
            limit = int(request.query_params.get("limit", 50))
        except (ValueError, TypeError):
            return Response(
                {"error": "Invalid limit param"}, status=status.HTTP_400_BAD_REQUEST
            )

        messages = list(Message.objects(room=room).order_by("-timestamp")[:limit])
        messages.reverse()
        return Response(MessageSerializer(messages, many=True).data)

    @action(detail=True, methods=["post"], url_path="read")
    def mark_as_read(self, request, pk=None):
        """
        Marks all messages in the room as read for the current user.
        """
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "room not found"}, status=status.HTTP_404_NOT_FOUND
            )

        self.check_object_permissions(request, room)

        unread = Message.objects(
            room=room, is_read=False, sender_id__ne=str(request.user.id)
        )
        ids = [str(m.id) for m in unread]
        unread.update(set__is_read=True)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            room.name,
            {
                "type": "messages_read",
                "user_id": str(request.user.id),
                "message_ids": ids,
            },
        )

        return Response(
            {
                "detail": f"{len(ids)} messages marked as read.",
                "message_ids": ids,
                "user_id": str(request.user.id),
            },
            status=status.HTTP_200_OK,
        )


class MessageViewSet(viewsets.ModelViewSet):
    """
    Messages (send).
    """

    serializer_class = MessageSerializer
    queryset = Message.objects.none()

    def get_permissions(self):
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        """
        Send a new message.
        Auto-creates room if it doesn't exist, but only investors can start a conversation.
        If room exists, both investor & startup can send a message.
        """
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        message_data = MessageSerializer(message).data

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            message.room.name,
            {"type": "chat_message", "message": message_data},
        )

        return Response(message_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        return Response(
            {"detail": "Use /rooms/<id>/messages/ to retrieve history."},
            status=status.HTTP_400_BAD_REQUEST,
        )
