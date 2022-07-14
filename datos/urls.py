from django.urls import path, re_path
from django.conf.urls import include

from datos.views import datosView, datosViewDetail

urlpatterns = [
    re_path(r'^datos/lista$', datosView.as_view()),
    re_path(r'^datos/(?P<pk>\d+)$', datosViewDetail.as_view()),
]