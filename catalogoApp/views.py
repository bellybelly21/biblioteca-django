from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Libro, Autor
from .forms import LibroForm, AutorForm
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import LibroSerializer, AutorSerializer
import json

def index(request):
    total_libros = Libro.objects.count()
    total_autores = Autor.objects.count()
    libros_disponibles = Libro.objects.filter(estado='Disponible').count()
    return render(request, 'index.html', {'total_libros': total_libros, 'total_autores': total_autores, 'libros_disponibles': libros_disponibles})

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})

def disponibles(request):
    libros_disponibles = Libro.objects.filter(estado='Disponible')
    return render(request, 'libros.html', {'libros': libros_disponibles})

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})

@login_required
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = LibroForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Agregar Libro'})

@login_required
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar Libro'})

@login_required
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('catalogo')
    return render(request, 'eliminar.html', {'libro': libro})

@login_required
def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Agregar Autor'})

class AutorViewSet(viewsets.ModelViewSet):

    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LibroViewSet(viewsets.ModelViewSet):

    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sincronizar_offline(request):
    try:
        registros = request.data.get('registros', [])
        
        if not registros:
            return Response({"error": "No se enviaron registros para sincronizar."}, status=status.HTTP_400_BAD_REQUEST)

        libros_creados = 0
        errores = []

        for item in registros:
            serializer = LibroSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                libros_creados += 1
            else:
                errores.append({"item": item, "errores": serializer.errors})

        return Response({
            "mensaje": "Sincronización procesada con éxito",
            "registros_guardados": libros_creados,
            "detalles_errores": errores
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": f"Error procesando los datos: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
