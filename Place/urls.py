from .views import PlaceViewSetModel
from django.conf.urls import url

place_list = PlaceViewSetModel.as_view({
    'get': 'list',
    'post': 'create'
})

place_detail = PlaceViewSetModel.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^$', place_list),
    url(r'^(?P<pk>[0-9]+)/$', place_detail),
]

