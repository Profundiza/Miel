from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = "menu"

urlpatterns = [
    url(r'^$', views.analisis, name='main'),
    url(r'^platillos/$', views.platillos, name='platillos'),
    url(r'^ingredientes/$', views.ingredientes, name='ingredientes'),
]
