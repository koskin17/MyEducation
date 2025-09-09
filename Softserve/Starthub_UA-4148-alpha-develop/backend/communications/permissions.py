from rest_framework.permissions import BasePermission
from .mongo_models import Room


class IsRoomParticipant(BasePermission):
    """
    Allows access only to participants of the given Room.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Room):
            return any(
                str(p.get("id")) == str(request.user.id) for p in obj.participants or []
            )
        return False
