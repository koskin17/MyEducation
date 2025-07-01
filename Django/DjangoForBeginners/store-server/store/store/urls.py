"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from products.views import index, products, test_context   # Импорт функции index из файла products/views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),   # Путь к главной странице сайта. Из-за пустого первого параметра ('') при переходе на наш сайт / проект будет открываться наша главная старница, которую мы описали как index и которая вызывается функцией index из файла products/views.py
    path('products/', products, name = 'products'),  # Путь к странице с товарами. В этом случае мы хотим, чтобы наша страница products открывалась по url-адресу со словом "products/" и из-за этого мы это указываем в качестве первого параметра в ''. При переходе на наш сайт / проект будет открываться страница с товарами, которую мы описали как products и которая вызывается функцией products из файла products/views.py
    path('test-context/', test_context, name = 'test_context'),
]
