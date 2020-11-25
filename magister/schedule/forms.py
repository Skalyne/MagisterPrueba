from django import forms
from .models import Profesores

class Profesform(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ('DNI','nombre','apellido','movil')

        widgets={
            'DNI': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI...'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'movil': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movil'}),
        }
        