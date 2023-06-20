from django.urls import path

from python_knight_app.views import index


urlpatterns = [
    path('', index),
]