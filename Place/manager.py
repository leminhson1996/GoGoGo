from django.contrib.gis.geos import GEOSGeometry


def get_place_by_segment(queryset, **kwargs):
    for key, value in kwargs.items():
        if key == 'name':
            queryset = queryset.filter(name__search=value)
        if key == 'address':
            queryset = queryset.filter(address__search=value)
    return queryset
