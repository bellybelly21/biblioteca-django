from django.contrib import admin
from .models import Libro, Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad')


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'codigo', 'genero', 'anio_publicacion', 'estado', 'autor')


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
