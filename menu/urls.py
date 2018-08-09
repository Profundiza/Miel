from django.conf.urls import url
from django.urls import path, include

from . import views
from . import export

app_name = "menu"

urlpatterns = [
    url(r'^$', views.analisis, name='main'),
    url(r'^proveedores/$', views.proveedores, name='proveedores'),
    url(r'^platillos/$', views.platillos, name='platillos'),
    url(r'^platillos/suprimir/$', views.del_platillo, name='platillos_delete'),
    url(r'^bebidas/$', views.bebidas, name='bebidas'),
    url(r'^ingredientes/$', views.ingredientes, name='ingredientes'),
    url(r'^ingredientes//?(?P<pk>[-\w\d]+)/?$', views.IngredienteUpdateView.as_view(), name='ingredientes_edit'),
    url(r'^ingredientes/suprimir/$', views.del_ingredient, name='ingredientes_delete'),
    url(r'^recetas/$', views.recetas, name='recetas'),
    url(r'^recetas//?(?P<pk>[-\w\d]+)/?$', views.recetas_modifier, name='recetas_edit'),
    url(r'^recetas/suprimir/$', views.del_receta, name='recetas_delete'),
    url(r'^exportar/$', export.export, name='export'),
]
