from django.shortcuts import render

from .models import *


def analisis(request):
    context = {}
    return render(request, 'menu/analisis.html', context)


def proveedores(request):
    return render(request, 'menu/proveedores.html')


def platillos(request):
    context = {}
    return render(request, 'menu/platillos.html', context)


def bebidas(request):
    return render(request, 'menu/bebidas.html')


def ingredientes(request):
    context = {
        'ingredientes': Ingrediente.objects.all(),
        'proveedores': Proveedor.objects.all(),
        'medidas': ['oz', 'lb', 'gal', 'L', 'mL', 'g', 'kg', 'unit', 'dozen']
    }
    # TODO medidas editable in admin
    return render(request, 'menu/ingredientes.html', context)


def add_ingredientes(request):
    name = request.GET['input-nombre']
    brand = request.GET['input-marca']
    proveedor = request.GET['input-proveedor']
    cost = request.GET['input-costo']
    measurement = request.GET['input-medida']
    quantity = request.GET['input-cantidad']


def recetas(request):
    return render(request, 'menu/recetas.html')
