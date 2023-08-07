from django.urls import path
from . import views

urlpatterns = [
    path('cars', views.cars, name='cars'),
    path('cars/<int:id>', views.OneCar, name='car'),
]
