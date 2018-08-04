from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = "menu"

urlpatterns = [
    url(r'^$', views.analisis, name='main'),
    url(r'^proveedores/$', views.proveedores, name='proveedores'),
    url(r'^proveedores/anadir/$', views.add_proveedor, name='proveedores_add'),
    url(r'^platillos/$', views.platillos, name='platillos'),
    url(r'^platillos/anadir/$', views.add_platillo, name='platillos_add'),
    url(r'^bebidas/anadir/$', views.add_platillo, name='bebidas_add'),
    url(r'^bebidas/$', views.bebidas, name='bebidas'),
    url(r'^ingredientes/$', views.ingredientes, name='ingredientes'),
    url(r'^ingredientes/$', views.ingredientes, name='ingredientes_sort'), #TODO change this
    url(r'^ingredientes/anadir/$', views.add_ingredient, name='ingredientes_add'),
    url(r'^recetas/$', views.recetas, name='recetas'),
    url(r'^recetas/anadir$', views.add_receta, name='recetas_add'),
]
