from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def handler404(request, exception):
    return render(request, '_404.html')


def home(request):
    return render(request, 'base.html')