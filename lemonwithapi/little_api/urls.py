from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('books/', views.books),
    path('', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view()),
]
