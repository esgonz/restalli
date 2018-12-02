from django import forms
from .models import Mesas

class MesasForm(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ['identificador', 'estado']
        widgets = {
            'identificador' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Mesa 01'}),
        }
        labels = {
            'identificador': 'Identificador(numero)', 
            'estado': 'Estado',
        }
