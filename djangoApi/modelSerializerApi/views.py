from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from modelSerializerApi.models import Athlete
from modelSerializerApi.serializer import AthleteSerializer
# Create your views here.


# class athlete(APIView):
#     def get(self, request):
#         # http://127.0.0.1:8000/api/class/characters/?author=west
#         items = Athlete.objects.all()
#         # return Response(items.values())
#         serialized_item = AthleteSerializer(items, many=True)
#         return Response(serialized_item.data)


class athlete(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


def delAthlete(request):
    Athlete.objects.all().delete()
