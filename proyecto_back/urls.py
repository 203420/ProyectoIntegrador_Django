from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^django/', include('datos.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
