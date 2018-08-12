from django.conf.urls import url
from django.urls import path, include

from . import views
from . import export

app_name = "menu"

urlpatterns = [
    url(r'^$', views.analisis, name='main'),
    url(r'^proveedores/$', views.proveedores, name='proveedores'),
    url(r'^proveedores/cambiar//?(?P<pk>[-\w\d]+)/?$', views.ProveedorUpdateView.as_view(), name='proveedores_edit'),
    url(r'^proveedores/error/$', views.proveedores_delete_error, name='proveedores_error'),
    url(r'^proveedores/suprimir//?(?P<pk>[-\w\d]+)/?$', views.del_proveedores, name='proveedores_delete'),
    url(r'^platillos/$', views.platillos, name='platillos'),
    url(r'^platillos/cambiar//?(?P<pk>[-\w\d]+)/?$', views.platillos_modifier, name='platillos_edit'),
    url(r'^platillos/suprimir/$', views.del_platillo, name='platillos_delete'),
    url(r'^bebidas/$', views.bebidas, name='bebidas'),
    url(r'^bebidas/cambiar//?(?P<pk>[-\w\d]+)/?$', views.platillos_modifier, name='bebidas_edit'),
    url(r'^ingredientes/$', views.ingredientes, name='ingredientes'),
    url(r'^ingredientes/cambiar//?(?P<pk>[-\w\d]+)/?$', views.IngredienteUpdateView.as_view(), name='ingredientes_edit'),
    url(r'^ingredientes/suprimir/$', views.del_ingredient, name='ingredientes_delete'),
    url(r'^recetas/$', views.recetas, name='recetas'),
    url(r'^recetas/cambiar//?(?P<pk>[-\w\d]+)/?$', views.recetas_modifier, name='recetas_edit'),
    url(r'^recetas/suprimir/$', views.del_receta, name='recetas_delete'),
    url(r'^exportar/$', export.export, name='export'),
]
