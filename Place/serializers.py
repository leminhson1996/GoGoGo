from rest_framework import serializers
from .models import PlaceInformation


class PlaceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceInformation
        fields = ('id', 'name', 'longitude', 'latitude', 'address', 'image', 'comments')
