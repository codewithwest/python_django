from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('books/', views.books, name="books"),
    path('new/book/', views.newBook, name="newBook"),
    path('delete/books/<int:pk>', views.deleteBook),

]
