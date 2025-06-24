from django.shortcuts import render

def home_view(request):
    return render(request, 'base.html')  # або 'home.html', якщо хочеш окремий шаблон
