from rest_framework import viewsets

from .serializers import PlaceInfoSerializer
from .models import PlaceInformation
from .manager import get_place_by_segment


class PlaceViewSetModel(viewsets.ModelViewSet):
    """
    ---
    list:
        Get all places
        parameters:
            - name: name
              description: Place's name
              required: true
              type: string
              paramType: query
    """

    serializer_class = PlaceInfoSerializer

    def get_queryset(self):
        queryset = PlaceInformation.objects.all()
        params = self.request.query_params
        return get_place_by_segment(queryset, **params)

