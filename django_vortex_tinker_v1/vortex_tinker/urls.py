from . import views
from . import forms
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('nav/', views.nav),
    path('profile', views.profile),
    path('method', views.method),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('forms', views.forms),
    path('menu_card/', views.menu_by_id),

]
