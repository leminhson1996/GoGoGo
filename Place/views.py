from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlaceInfoSerializer
from .models import PlaceInformation


class PlaceViewSetModel(viewsets.ModelViewSet):
    serializer_class = PlaceInfoSerializer
    queryset = PlaceInformation.objects.all()

