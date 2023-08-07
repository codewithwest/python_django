from django.urls import path
from . import views

urlpatterns = [
    path('', views.athlete.as_view(), name="athlete"),
    path('del', views.delAthlete, name="del")
]
