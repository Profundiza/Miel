from django.shortcuts import render


def analiticos(request):
    context = {}
    return render(request, 'menu/analiticos.html', context)


def platillos(request):
    context = {}
    return render(request, 'menu/platillos.html', context)


def ingredientes(request):
    context = {}
    return render(request, 'menu/ingredientes.html', context)
