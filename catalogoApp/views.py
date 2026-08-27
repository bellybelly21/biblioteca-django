from django.shortcuts import render
from . import models

def libros(request):
    data = {
        'libros': models.libros
        }
    return render (request, 'catalogoApp.html', data)

def disponibles(request):
    libros_disponibles = []

    for libro in models.libros:
        if libro['estado'] == 'Disponible':
            libros_disponibles.append(libro)

    data = {
        'libros': libros_disponibles
    }

    return render(request, 'catalogoApp.html', data)