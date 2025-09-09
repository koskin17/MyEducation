from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, get_user_model, login
from django.views.decorators.http import require_http_methods
from rest_framework_simplejwt.tokens import RefreshToken

from .mongo_models import Room, Message
from .utils.generate_room_name import generate_room_name

import logging

User = get_user_model()

# Get logger for this module
logger = logging.getLogger(__name__)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "chat/login.html")


def login_htmx(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    user = authenticate(request, email=email, password=password)
    if not user:
        return HttpResponse("<div class='error'>Invalid credentials</div>", status=401)

    login(request, user)
    refresh = RefreshToken.for_user(user)
    access = str(refresh.access_token)

    return HttpResponse(
        f"""
        <script>
            localStorage.setItem("access", "{access}");
            localStorage.setItem("refresh", "{str(refresh)}");
            window.location.href = "/chat/";
        </script>
    """
    )


def index(request):
    """
    Render the js landing page.
    Investor: lists startups with 'start/continue' buttons.
    Startup: lists existing conversations only.
    """
    if request.GET.get("force_logout") == "1":
        from django.contrib.auth import logout

        logout(request)
        return redirect("login")

    user = request.user
    print(f"💡 Authenticated? {user.is_authenticated}, User: {user}")

    if not user.is_authenticated:
        return redirect("login")
    if request.GET.get("force_logout") == "1":
        from django.contrib.auth import logout

        logout(request)
        return redirect("login")

    if user.role.role == "investor":
        startups = list(User.objects.filter(role__role="startup"))
        rooms = {r.name: r for r in Room.objects(participants__id=str(user.id))}

        def startup_has_room(startup):
            for room in rooms.values():
                for p in room.participants:
                    if str(p.get("id")) == str(startup.id):
                        return True
            return False

        startups.sort(key=lambda s: not startup_has_room(s))
    elif user.role.role == "startup":
        rooms = Room.objects(participants__id=str(user.id)).order_by("-updated_at")
    else:
        return HttpResponseForbidden("Unknown role, please contact admin")

    if user.role.role == "investor":
        return render(
            request,
            "chat/investor_index.html",
            {
                "startups": startups,
                "rooms": rooms,
            },
        )
    elif user.role.role == "startup":
        return render(request, "chat/startup_index.html", {"rooms": rooms})


def room(request, room_id):
    """
    Shows conversation room with messages.
    """
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        raise Http404("Room not found")

    if str(request.user.id) not in [p["id"] for p in room.participants]:
        raise Http404("You are not a participant in this room.")

    other_participant = None
    for participant in room.participants:
        if participant["id"] != str(request.user.id):
            other_participant = participant
            break

    context = {
        "room": room,
        "user": request.user,
        "other_participant": other_participant,
    }
    return render(request, "chat/room.html", context)


def serialize_user(user):
    return {
        "id": str(user.id),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }


@require_http_methods(["GET"])
def start_conversation(request, other_user_id):
    user = request.user
    other_user = get_object_or_404(User, id=other_user_id)

    room_name = generate_room_name(user, other_user)

    room = Room.objects(name=room_name).first()
    if not room:
        room = Room(
            name=room_name,
            participants=[serialize_user(user), serialize_user(other_user)],
        )
        room.save()

    return redirect("room", room_id=room.id)
