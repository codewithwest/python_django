from django.shortcuts import render
from .data import characters_list

# Create your views here.


def home(request):
    return render(request, 'routes/index.html')


def shop(request):
    return render(request, 'routes/shop.html')


def about(request):
    return render(request, 'routes/about.html')


def login(request):
    return render(request, 'routes/auth/login.html')


def register(request):
    return render(request, 'routes/auth/register.html')


def characters(request):
    return render(request, 'routes/characters.html', {'characters': characters_list})
