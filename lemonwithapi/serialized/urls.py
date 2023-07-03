from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('menu_items/', views.menu_items),
    path('menu_items/<int:id>', views.menu_item),
    # path('', views.BookList.as_view()),
    # path('books/<int:pk>', views.Book.as_view()),
]
