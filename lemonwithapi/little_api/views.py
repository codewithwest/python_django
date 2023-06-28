from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.


def handler404(request, exception):
    return render(request, '_404.html')


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
