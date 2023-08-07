from django.shortcuts import render
# Import generics from drf
from rest_framework import generics
# get the models
from .models import MenuItem
# get the serializers
from .serializers import MenuItemSerializer
# Create your views here.

# Entend list create view from generics


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
