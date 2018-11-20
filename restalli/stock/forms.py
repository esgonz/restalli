from django import forms
from .models import ProductoStock, Stock, CategoriaStock

class StockForm(forms.ModelForm):
    class Meta:
        model = ProductoStock
        fields = ['nombreProducto', 'codigo','porcion', 'unidadMedida', 'precio', 'fechaElaboracion', 'fechaExpiracion','categoria_uuid', 'status']
        widgets = {
            'nombreProducto' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre1'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte Codigo'}),
            'porcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Porcion'}),
            'unidadMedida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medida'}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'fechaElaboracion': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de elaboración '}),
            'fechaExpiracion': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de ex '}),
            'categoria_uuid': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'status'})
        }
        labels = {
            'nombreProducto': 'Nombre', 'codigo': 'Codigo', 'porcion': 'Porcion',
             'unidadMedida': 'Medida', 'precio': 'Precio', 'fechaElaboracion': '', 'fechaExpiracion': '', 'categoria_uuid': '', 'status': ''
        }
class CatForm(forms.ModelForm):
    class Meta:
        model = CategoriaStock
        fields = ['nombreCategoria','status', 'user_uuid']
        widgets = {
            'nombreCategoria' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte estado'}),
            'user_uuid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario'}),
        }     
class StocklogForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['producto_uuid', 'stockInicial','StockDescontado', 'StockFinal', 'status', 'user_uuid']
        widgets = {
            'producto_uuid' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'producto'}),
            'stockInicial' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inicial'}),
            'StockDescontado' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descontado'}),
            'StockFinal' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Final'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte estado'}),
            'user_uuid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario'}),
            
        }        

