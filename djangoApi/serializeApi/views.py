from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Car
from .serializers import CarSerializer
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(['GET', 'POST'])
def cars(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        barcode = get_random_string(length=128)

        car = Car(
            name=name,
            type=type,
            price=price,
            inventory=inventory,
            barcode=barcode
        )
        # Trys to save and send response
        try:
            car.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        return Response()
    else:
        items = Car.objects.all()
        # return Response(items.values())
        serialized_item = CarSerializer(items, many=True)
        return Response(serialized_item.data)


@api_view()
def OneCar(request, id):
    # item = Car.objects.get(pk=id)
    item = get_object_or_404(Car, pk=id)
    serialized_item = CarSerializer(item)
    return Response(serialized_item.data)
