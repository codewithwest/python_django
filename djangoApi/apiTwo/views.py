from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


@api_view(['GET', 'POST'])
def characters(request):
    return Response('List of The Books', status=status.HTTP_200_OK)


# Class Based View
class Characters(APIView):
    def get(self, request):
        # http://127.0.0.1:8000/api/class/characters/?author=west
        author = request.GET.get('author')
        if (author):
            return Response({"Message": "List of all the Characters by "+author}, status.HTTP_200_OK)
        return Response({"Message": "List of all the Characters"}, status.HTTP_200_OK)

    def post(self, request):
        return Response({"title": request.data.get('title')}, status.HTTP_201_CREATED)


class Book(APIView):
    def get(self, request, pk):
        return Response({"message": "Single book with id "+str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({"title": request.data.get('title')}, status.HTTP_201_CREATED)

# class BookView(APIView):
#     def get(self, request, pk):
#         return Response({"message": "single book with id " + str(pk)}, status.HTTP_200_OK)

#     def put(self, request, pk):
#         return Response({"title": request.data.get('title')}, status.HTTP_200_OK)


# urlpatterns = [
#   path('books/<int:pk>',views.BookView.as_view())
# ]


# Routing classes that extend viewsets
# You can have classes that extend the different
# types of ViewSets in your API project.
# Just like the classes that extend APIView,
# these classes also have specific methods used
#  to respond to different types of HTTP requests.
# Here’s an example of a typical class that extends
# the viewset.Viewset class.

# Class BookView(viewsets.ViewSet):
# 	def list(self, request):
#     	return Response({"message":"All books"}, status.HTTP_200_OK)
# 	def create(self, request):
#     	return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
# 	def update(self, request, pk=None):
#     	return Response({"message":"Updating a book"}, status.HTTP_200_OK)
# 	def retrieve(self, request, pk=None):
#     	return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
# 	def partial_update(self, request, pk=None):
#         return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
# 	def destroy(self, request, pk=None):
#     	return Response({"message":"Deleting a book"}, status.HTTP_200_OK)

#  You can map this class in the urls.py
# file in your Django app as follows.

# urlpatterns = [
# 	path('books', views.BookView.as_view(
#     	{
#         	'get': 'list',
#         	'post': 'create',
#     	})
# 	),
#     path('books/<int:pk>',views.BookView.as_view(
#     	{
#         	'get': 'retrieve',
#         	'put': 'update',
#         	'patch': 'partial_update',
#         	'delete': 'destroy',
#     	})
# 	)
# ]
