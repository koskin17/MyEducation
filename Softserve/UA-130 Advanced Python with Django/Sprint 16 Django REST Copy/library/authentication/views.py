import time
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from rest_framework import viewsets
from authentication.models import CustomUser
from authentication.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        if 'guest' in request.POST:
            return redirect('guest')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            if user.role == 1:
                return redirect('profile', user_id=user.id)
            elif user.role == 2:
                return redirect('guest')
            else:
                return redirect('login') 
        else:
            return render(request, 'authentication/login.html', {'error': 'Wrong data!'})
    return render(request, 'authentication/login.html')


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            role=1, 
            is_active=True
        )
        
        return redirect('login')
    return render(request, 'authentication/register.html')


def librarians_view(request):
    if not request.user.is_authenticated or request.user.role != 1:
        messages.error(request, "You must be a registered user to view all librarians.")
        return redirect('login')

    email_query = request.GET.get('email')
    if email_query:
        librarians = User.objects.filter(role=1, email__iexact=email_query)
    else:
        librarians = User.objects.filter(role=1)

    return render(request, 'authentication/librarians.html', {'librarians': librarians})


def guest_view(request):
    if not request.user.is_authenticated:
        unique_email = f'guest_{int(time.time())}@example.com'
        guest_user = User.objects.create_user(
            email=unique_email,
            password=User.objects.make_random_password(),
            first_name='Guest',
            last_name='User',
            middle_name='',
            role=2, 
            is_active=True
        )
        login(request, guest_user)
    elif request.user.role != 2:
        return redirect('profile', user_id=request.user.id)

    return render(request, 'authentication/guest.html')


def profile_view(request, user_id):
    if not request.user.is_authenticated or request.user.role != 1:
        return redirect('guest')

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('guest')

    return render(request, 'authentication/profile.html', {'user': user})


def logout_view(request):
    logout(request)
    return redirect('base')