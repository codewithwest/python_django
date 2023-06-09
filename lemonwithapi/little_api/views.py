from rest_framework import serializers
from . import views
from django.urls import path
from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


# def handler404(request, exception):
#     return render(request, '_404.html')


@api_view(['GET', 'POST'])
# def home(request):
#     return Response(request, 'base.html')
def books(request):
    return Response('List of all books',
                    status=status.HTTP_200_OK)


class BookList(APIView):

    def get(self, request):
        author = request.GET.get('author')
        return Response({'messase: "Response Books List ' + author}, status.HTTP_200_OK)

    def post(self, request):
        return Response({'title': request.data.get('title')}, status.HTTP_201_CREATED)


class Book(APIView):
    def get(self, request, pk):
        # author = request.GET.get('author')
        return Response({'messase: "Response Books List ' + str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({'title': request.data.get('title')}, status.HTTP_200_OK)


# Lab on  DRF

# Solution code for models.py

# Create your models here.

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=5, decimal_places=2)


# Solution code for views.py
from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.


# class BookView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class SingleBookView(generics.RetrieveUpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# Solution code for urls.py (Project-level)
# from django.contrib import admin
# from django.urls import path, include


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('BookListDRF.urls')),
# ]


# Solution code for urls.py (App-level)

# urlpatterns = [
#     path('books', views.BookView.as_view()),
    # path('books/<int:pk>', views.SingleBookView.as_view()),
# ]

# Solution code for serializers.py
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'price']
def home(request):
    return render(request, 'base.html')


# Create your views here.
@csrf_exempt
def books(request):
    # Checks method type
    if request.method == 'GET':
        # Retrieves all Book Model entries
        books = Book.objects.all().values()
        # Returns all Book entries in json format
        return JsonResponse({"books": list(books)})
    # Check if post
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        # Creates new book
        book = Book(
            title=title,
            author=author,
            price=price
        )
        try:
            # saves book entry
            book.save()

        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        return JsonResponse(model_to_dict(book), status=201)
