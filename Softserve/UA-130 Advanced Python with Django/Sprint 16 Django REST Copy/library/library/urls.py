"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from authentication import views as auth_views
from views import home_view
from book.views import create_book


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),  # Connects other routes for authentication
    path('', home_view, name='base'), # Main page
    path('librarians/', auth_views.librarians_view, name='librarians'),
    path('author/', include('author.urls')),
    path('book/', include('book.urls')),
    path('order/', include('order.urls')),
    path('add/', create_book, name='book_form.html'),
    path('api/v1/', include('api.urls')),  # connect REST API
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
