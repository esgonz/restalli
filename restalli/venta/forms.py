from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['tipoPago', 'stockInicial','status',  'user_uuid']
        widgets = {
          
            
        }        