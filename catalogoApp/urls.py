from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.libros, name='catalogo'),
    path('catalogo/disponibles/', views.disponibles, name='disponibles')
]
