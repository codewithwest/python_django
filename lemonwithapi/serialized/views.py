from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MemuItems
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MemuItems.objects.all()
        serialize_items = MenuItemSerializer(items, many=True)
        return Response(serialize_items.data)
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view()
 throttle_classe = [AnonRateThrottle, UserRateThrottle]
@throttle_classes([throttle_classe])
def menu_item(request, id):
    # item = MemuItems.objects.get(pk=id)
    item = get_object_or_404(MemuItems, pk=id)

    serialize_items = MenuItemSerializer(item)
    return Response(serialize_items.data)
