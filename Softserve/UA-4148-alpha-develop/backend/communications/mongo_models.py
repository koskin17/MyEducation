import datetime

from mongoengine import (
    CASCADE,
    BooleanField,
    DateTimeField,
    DictField,
    Document,
    IntField,
    ListField,
    ReferenceField,
    StringField,
)


class Room(Document):
    """
    Represents a chat room between one or more participants.
    Stores denormalized participant data to avoid frequent lookups in Postgres.
    """

    meta = {
        "db_alias": "chat_db",
        "collection": "rooms",
        "indexes": [
            "name",
            {"fields": ["participants"]},
        ],
    }

    name = StringField(required=True, unique=True)
    participants = ListField(
        DictField(
            fields={
                "id": StringField(required=True),
                "username": StringField(),
                "first_name": StringField(),
                "last_name": StringField(),
            }
        ),
        default=[],
    )
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow()
        return super().save(*args, **kwargs)

    def add_participant(self, user_id, username, first_name, last_name):
        uid = str(user_id)
        if not any(p["id"] == uid for p in self.participants):
            self.participants.append(
                {
                    "id": uid,
                    "username": username,
                    "first_name": first_name,
                    "last_name": last_name,
                }
            )
            self.save()


class Message(Document):
    """
    Represents a message sent within a chat room.
    Stores sender info denormalized for fast retrieval without Postgres queries.
    """

    meta = {
        "db_alias": "chat_db",
        "collection": "messages",
        "indexes": [("room", "timestamp"), "-timestamp"],
    }

    room = ReferenceField(Room, reverse_delete_rule=CASCADE, required=True)
    sender_id = StringField(required=True)
    sender_first_name = StringField()
    sender_last_name = StringField()
    text = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)
    is_read = BooleanField(default=False)
