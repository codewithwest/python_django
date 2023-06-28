from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home),
    path('books', views.books),
    # path('api/', include('BookListAPI.urls')),
]
