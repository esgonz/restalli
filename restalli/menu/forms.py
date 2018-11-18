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
		'status',
		'categoria_uuid'] # list of fields you want from model
		widgets = {
        	'descripcion': forms.Textarea(attrs={'cols': 5, 'rows': 4}),
        }
    #nombreProducto =  forms.CharField()
    #descripcion = forms.CharField(widget=forms.Textarea)
