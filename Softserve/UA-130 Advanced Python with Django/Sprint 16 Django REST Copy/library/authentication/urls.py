from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),  # authentication/
    path('librarians/', views.librarians_view, name='librarians'),
    path('register/', views.register_view, name='register'),  # authentication/register/
    path('guest/', views.guest_view, name='guest'),  # authentication/guest/
    path('logout/', views.logout_view, name='logout'),  # authentication/logout/
    path('<int:user_id>/', views.profile_view, name='profile'),  # /authentication/user_name
    path('login/', views.login_view, name='login_explicit'),
]
