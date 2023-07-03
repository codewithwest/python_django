from django.urls import include, path
from . import views

urlpatterns = [
    path('books/', views.books),
    path('', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view()),
    path('books', views.books),
    # path('api/', include('BookListAPI.urls')),
]
