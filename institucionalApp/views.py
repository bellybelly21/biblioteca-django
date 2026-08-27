from django.shortcuts import render
from . import models


def institucional(request):
    return render(request, 'institucionalApp.html')


def actividades(request):
    data = {
        'actividades': models.actividades
    }

    return render(request, 'actividades.html', data)
