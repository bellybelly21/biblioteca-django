from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.listar_libros, name='catalogo'),
    path('catalogo/disponibles/', views.disponibles, name='disponibles'),
    path('catalogo/nuevo/', views.agregar_libro, name='agregar_libro'),
    path('catalogo/editar/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('catalogo/eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/nuevo/', views.agregar_autor, name='agregar_autor'),
]