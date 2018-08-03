from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

# TODO medidas editable in admin
# TODO constants file
MEDIDAS = ['oz', 'lb', 'gal', 'L', 'mL', 'g', 'kg', 'unit', 'dozen']


def analisis(request):
    context = {}
    return render(request, 'menu/analisis.html', context)


def proveedores(request):
    context = {
        'proveedores': Proveedor.objects.all(),
    }
    return render(request, 'menu/proveedores.html', context)


def add_proveedor(request):
    fields = {
        'name': request.POST['input-nombre'],
        'phone': request.POST['input-phone'],
        'sales_rep': request.POST['input-rep'],
        'sales_rep_phone': request.POST['input-rep_phone'],
        'email': request.POST['input-email'],
    }
    Proveedor.objects.create(**fields)
    return HttpResponseRedirect(reverse('menu:proveedores'))


def platillos(request):
    context = {}
    return render(request, 'menu/platillos.html', context)


def bebidas(request):
    return render(request, 'menu/bebidas.html')


def ingredientes(request):
    # TODO add current user's restaurant
    context = {
        'restaurante': '',
        'ingredientes': Ingrediente.objects.all(),
        'proveedores': Proveedor.objects.all(),
        'medidas': MEDIDAS
    }
    return render(request, 'menu/ingredientes.html', context)


def add_ingredient(request):
    # TODO add current user's restaurant
    fields = {
        'restaurante': '',
        'name': request.POST['input-nombre'],
        'brand': request.POST['input-marca'],
        'proveedor': Proveedor.objects.get(id=request.POST['input-proveedor']),
        'cost': request.POST['input-costo'],
        'measurement': request.POST['input-medida'],
        'quantity': request.POST['input-cantidad']
    }
    Ingrediente.objects.create(**fields)
    return HttpResponseRedirect(reverse('menu:ingredientes'))


def recetas(request):
    context = {
        'recetas': Receta.objects.all(),
        'ingredientes': Ingrediente.objects.all(),
        'medidas': MEDIDAS
    }
    return render(request, 'menu/recetas.html', context)


def add_receta(request):
    hi = "hi"
    fields = {
        'restaurante': '',
        'name': request.POST['input-nombre'],
        # TODO fix ingrediente filter
        'ingredientes': Ingrediente.objects.filter(id in request.POST['input-ingredientes'])
    }
    return HttpResponseRedirect(reverse('menu:recetas'))
