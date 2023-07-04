from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('about/', views.about, name="about"),
    path('characters/', views.characters, name="characters"),
    # Auth Routes
    path('user/auth/login', views.login, name="login"),
    path('user/auth/register', views.register, name="register"),
]
