from django.shortcuts import render
from . import models

def encargados(request):
    data = {
        'encargados': models.encargados
    }
    return render(request, 'personalApp.html', data)
