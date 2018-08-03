from django.shortcuts import render


def analisis(request):
    context = {}
    return render(request, 'menu/analisis.html', context)


def proveedores(request):
    return render(request, 'menu/proveedores.html')


def platillos(request):
    context = {}
    return render(request, 'menu/platillos.html', context)


def ingredientes(request):
    context = {}
    return render(request, 'menu/ingredientes.html', context)
