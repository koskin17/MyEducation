from django import template

register = template.Library()


@register.filter
def get_other_user(participants, current_user):
    """
    Given a list of participants, return the other user's username (or object).
    """
    for p in participants:
        if str(p.get("id")) != str(current_user.id):
            first = p.get("first_name", "")
            last = p.get("last_name", "")
            full_name = f"{first} {last}".strip()
            return full_name or p.get("username") or p.get("id")
    return "Unknown"


@register.filter
def get_room_id(rooms, other_user_id):
    """
    Given a dict of rooms (keyed by name), find the room id
    where the other_user_id is part of the participants.
    """
    for room in rooms.values():
        for p in room.participants:
            if str(p.get("id")) == str(other_user_id):
                return room.id
    return None
