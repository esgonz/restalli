from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['tipoPago','identificador', 'monto', 'monto_propina', 'pedido_uuid']
        labels = {
        	'tipoPago': 'Tipo de Pago',
        	'identificador': 'Código (Transbank ó Boleta)', 
        	'monto': 'Monto total pedido', 
        	'monto_propina': 'Propina sugerida', 
        	'pedido_uuid': 'Pedido'
        

        }    