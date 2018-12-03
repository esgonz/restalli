from django import forms
from .models import Pedido, PedidoItem

class PedidoForm(forms.ModelForm):


	class Meta:
		model = Pedido
		fields = [
		'estadoPedido',
		'mesa'
		]
    	#nombreProducto =  forms.CharField()
    	#descripcion = forms.CharField(widget=forms.Textarea)
		widgets = {
        	'total': forms.TextInput(attrs={ 'type':"hidden"}),
        }


class PedidoItemForm(forms.ModelForm):
	class Meta:
		model = PedidoItem
		fields = [
		'productoMenu',
		'cantidad',
		'precioVenta',
		'subtotal',
		'estadoPedido',
		'pedido_uuid'] # list of fields you want from model
    #nombreProducto =  forms.CharField()
    #descripcion = forms.CharField(widget=forms.Textarea)
