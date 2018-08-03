from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def analisis(request):
    context = {}
    return render(request, 'menu/analisis.html', context)


def proveedores(request):
    context = {
        'proveedores': Proveedor.objects.all(),
    }
    return render(request, 'menu/proveedores.html', context)


def add_proveedores(request):
    fields = {
        'name': request.POST['input-nombre'],
        'phone': request.POST['input-phone'],
        'sales_rep': request.POST['input-rep'],
        'sales_rep_phone': request.POST['input-rep_phone'],
        'email': request.POST['input-email'],
    }
    Proveedor.objects.create(fields)
    return HttpResponseRedirect(reverse('menu:proveedor'))


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
    fields = {
        'name': request.POST['input-nombre'],
        'brand': request.POST['input-marca'],
        'proveedor': request.POST['input-proveedor'],
        'cost': request.POST['input-costo'],
        'measurement': request.POST['input-medida'],
        'quantity': request.POST['input-cantidad']
    }
    ingrediente = Ingrediente.objects.create(fields)
    return HttpResponseRedirect(reverse('menu:ingredientes'))


def recetas(request):
    return render(request, 'menu/recetas.html')
