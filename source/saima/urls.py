from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^alfreds', views.alfred_list),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




