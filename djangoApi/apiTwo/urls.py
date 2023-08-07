from django.urls import path

from . import views

urlpatterns = [
    path('characters/', views.characters),
    path('class/characters/', views.Characters.as_view()),
    path('book/<int:pk>', views.Book.as_view()),

]
