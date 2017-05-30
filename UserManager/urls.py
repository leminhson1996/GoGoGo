from .views import UserViewSet
from django.conf.urls import url

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^$', user_list),
    url(r'^(?P<pk>[0-9]+)/$', user_detail),
]

