from django.urls import path

from .views import index, room, login_page, login_htmx, start_conversation

urlpatterns = [
    path("login/", login_page, name="login"),
    path("login/submit/", login_htmx, name="login_htmx"),
    path("", index, name="index"),
    path("room/<str:room_id>/", room, name="room"),
    path("start/<str:other_user_id>/", start_conversation, name="start-conversation"),
]
