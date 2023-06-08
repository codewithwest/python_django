from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('profile', views.profile),
    path('method', views.method),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
]
