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
        'proveedores': Proveedor.objects.all()
    }
    return render(request, 'menu/ingredientes.html', context)


def recetas(request):
    return render(request, 'menu/recetas.html')
