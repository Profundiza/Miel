from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *

# TODO medidas editable in admin
# TODO constants file
MEDIDAS = ['oz', 'lb', 'gal', 'L', 'mL', 'g', 'kg', 'unit', 'dozen']


def analisis(request):
    context = {}
    return render(request, 'menu/analisis.html', context)


def proveedores(request):
    prov = Proveedor.objects.filter(restaurante__id=request.user.restaurante.id)
    context = {
        'proveedores': prov,
    }
    return render(request, 'menu/proveedores.html', context)


def add_proveedor(request):
    fields = {
        'restaurante': request.user.restaurante,
        'name': request.POST['input-nombre'],
        'phone': request.POST['input-phone'],
        'sales_rep': request.POST['input-rep'],
        'sales_rep_phone': request.POST['input-rep_phone'],
        'email': request.POST['input-email'],
    }
    Proveedor.objects.create(**fields)
    return HttpResponseRedirect(reverse('menu:proveedores'))


def platillos(request):
    rest = request.user.restaurante
    plats = Platillo.objects.filter(restaurante__id=rest.id, bebida=False)
    context = {
        'restaurante': rest,
        'platillos': plats,
        'ingredientes': Ingrediente.objects.filter(restaurante__id=rest.id),
        'recetas': Receta.objects.filter(restaurante__id=rest.id),
        'tipo': 'platillo'
    }
    return render(request, 'menu/platillos.html', context)


def add_platillo(request):
    mi_ingredientes = Ingrediente.objects.filter(pk__in=request.POST.getlist('added-ing'))
    mi_recetas = Receta.objects.filter(pk__in=request.POST.getlist('added-rec'))

    fields = {
        'restaurante': request.user.restaurante,
        'nombre': request.POST['input-nombre'],
        'precio': request.POST['input-precio'],
        'bebida': 'bebidas' in request.resolver_match.view_name
    }
    cost = 0
    platillo = Platillo.objects.create(**fields)
    for ing in mi_ingredientes:
        q = request.POST['ing-'+ing.id]
        ing_fields = {
            'platillo': platillo,
            'ingrediente': ing,
            'quantity': q
        }
        cost += ing.unit_cost * q
        PlatilloRec.objects.create(**ing_fields)
    for rec in mi_recetas:
        q = request.POST['rec-'+rec.id]
        rec_fields = {
            'platillo': platillo,
            'receta': rec,
            'quantity': q
        }
        cost += rec.unit_cost * q
        PlatilloRec.objects.create(**rec_fields)

    if 'bebidas' in request.resolver_match.view_name:
        redirect_to = 'menu:bebidas'
    else:
        redirect_to = 'menu:platillos'
    return redirect(redirect_to)


def bebidas(request):
    rest = request.user.restaurante
    plats = Platillo.objects.filter(restaurante__id=rest.id, bebida=True)
    context = {
        'tipo': 'bebida',
        'restaurante': rest,
        'platillos': plats,
        'ingredientes': Ingrediente.objects.filter(restaurante__id=rest.id),
        'recetas': Receta.objects.filter(restaurante__id=rest.id)
    }
    return render(request, 'menu/platillos.html', context)


def ingredientes(request):
    # TODO add current user's restaurant
    context = {
        'restaurante': request.user.restaurante,
        'ingredientes': Ingrediente.objects.filter(restaurante__id=request.user.restaurante.id),
        'proveedores': Proveedor.objects.filter(restaurante__id=request.user.restaurante.id),
        'medidas': MEDIDAS
    }
    return render(request, 'menu/ingredientes.html', context)


def add_ingredient(request):
    # TODO add current user's restaurant
    fields = {
        'restaurante': request.user.restaurante,
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
        'recetas': Receta.objects.filter(restaurante__id=request.user.restaurante.id),
        'ingredientes': Ingrediente.objects.filter(restaurante__id=request.user.restaurante.id),
        'medidas': MEDIDAS
    }
    return render(request, 'menu/recetas.html', context)


def add_receta(request):
    mi_ingredientes = Ingrediente.objects.filter(pk__in=request.POST.getlist('added-ing'))
    fields = {
        'restaurante': request.user.restaurante,
        'name': request.POST['input-nombre'],
        'measurement': request.POST['input-medida'],
        'quantity': request.POST['input-cantidad'],
    }

    cost = 0
    receta = Receta.objects.create(**fields)
    for ing in mi_ingredientes:
        ing_fields = {
            'receta': receta,
            'ingrediente': ing,
            'quantity': request.POST['ing-'+ing.id]
        }
        cost += ing.cost
        RecetaComp.objects.create(**ing_fields)

    receta.cost = cost
    receta.save()

    return HttpResponseRedirect(reverse('menu:recetas'))
