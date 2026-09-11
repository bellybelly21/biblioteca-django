from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Producto
class Libro(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=80)
    anio_publicacion = models.PositiveIntegerField()
    estado = models.CharField(max_length=20)
    autor = models.ForeignKey(Autor, on_delete=models.RESTRICT)

    def __str__(self):
            return self.titulo
