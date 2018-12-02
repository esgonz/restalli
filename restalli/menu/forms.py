from django import forms
from .models import ProductosMenu, CategoriaMenu, ProductosMenuStock

class ProductosMenuForm(forms.ModelForm):
	class Meta:
		model = ProductosMenu
		fields = [
		'nombre',
		'descripcion',
		'imagen',
		'precio',
		'categoria_uuid'] # list of fields you want from model
		widgets = {
        	'descripcion': forms.Textarea(attrs={'cols': 5, 'rows': 4}),
        	'descripcion': forms.TextInput(attrs={'min': 0, 'type':"number"}),
        }
    #nombreProducto =  forms.CharField()
    #descripcion = forms.CharField(widget=forms.Textarea)



class ProductosMenuStockForm(forms.ModelForm):
	class Meta:
		model = ProductosMenuStock
		fields = [
		'productoStock_uuid',
		'productosMenu_uuid',
		'porciones'] # list of fields you want from model
    #nombreProducto =  forms.CharField()
    #descripcion = forms.CharField(widget=forms.Textarea)
