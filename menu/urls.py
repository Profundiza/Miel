from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = "menu"

urlpatterns = [
    url(r'^$', views.analisis, name='main'),
    url(r'^proveedores/$', views.proveedores, name='proveedores'),
    url(r'^proveedores/add/$', views.add_proveedores, name='proveedores_add'),
    url(r'^platillos/$', views.platillos, name='platillos'),
    url(r'^bebidas/$', views.bebidas, name='bebidas'),
    url(r'^ingredientes/$', views.ingredientes, name='ingredientes'),
    url(r'^ingredientes/$', views.ingredientes, name='ingredientes_sort'), #TODO change this
    url(r'^ingredientes/add/$', views.add_ingredientes, name='ingredientes_add'),
    url(r'^recetas/$', views.recetas, name='recetas'),
]
