from django.shortcuts import render,redirect

# Create your views here.
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
def books(request):
    # Checks methos type
    if request.method == 'GET':
        # Gets all data that matches the model
        books = Book.objects.all().values()
        # Returns it as a list
        return render(request, 'routes/allbooks.html',{"books":list(books)})
        # return JsonResponse({"books":list(books)})

    
@csrf_exempt
def newBook(request):
     # Checks methos type
    if request.method == 'GET':
        # Gets all data that matches the model
         
        # Returns it as a list
        return render(request, 'routes/newbook.html')
        # return JsonResponse({"books":list(books)})
    elif request.method == 'POST':
        # If method is post then adds to database of the set data
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price'))
        book = Book(
            title = title,
            author = author,
            price = price
        )
        # Trys to save and send response
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return HttpResponseRedirect('/api/books/')
