from django import forms
from .models import Libro, Autor

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'anio_publicacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-select'})
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }