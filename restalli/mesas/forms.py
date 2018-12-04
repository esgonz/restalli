from django import forms
from .models import Mesas

class MesasForm(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ['identificador', 'estado', 'pedido', 'empleado', 'fecha', 'inicio', 'termino','status']
        widgets = {
            'identificador' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte Codigo'}),
            'pedido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Porcion'}),
            'empleado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medida'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'inicion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de elaboración '}),
            'termino': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Expiración '}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'status'})
        }
        labels = {
            'identificador': '', 'estado': '', 'pedido': '', 'empleado': '', 'fecha': '', 'inicio': '', 'termino': '', 'status': ''
        }