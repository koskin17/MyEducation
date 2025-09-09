def generate_room_name(user1, user2):
    """
    Generates a unique room name based on user roles: {investor_id}_{startup_id}.
    """

    def get_role_name(user):
        return getattr(user.role, "role", None)

    role1 = get_role_name(user1)
    role2 = get_role_name(user2)

    if {role1, role2} != {"investor", "startup"}:
        raise ValueError("Room can only be generated between investor and startup")

    investor = user1 if role1 == "investor" else user2
    startup = user2 if role1 == "investor" else user1

    return f"{investor.id}_{startup.id}"
