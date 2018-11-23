from django import forms
from .models import ProductoStock, Stock, CategoriaStock
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class StockForm(forms.ModelForm):
    class Meta:
        model = ProductoStock
        fields = ['nombreProducto', 'codigo','porcion', 'unidadMedida', 'precio', 
        'fechaElaboracion', 'fechaExpiracion','categoria_uuid', 'status']
        widgets = {
        'fechaElaboracion': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
        'fechaExpiracion' : forms.DateInput(attrs={'type':'date', 'class': 'form.control'})
        
        }
                        
        

    labels = {
            'nombreProducto': 'Nombre', 'codigo': 'Codigo', 'porcion': 'Porcion',
             'unidadMedida': 'Medida', 'precio': 'Precio', 'fechaElaboracion': '("Choose Year", "Choose Month", "Choose Day")', 'fechaExpiracion': '', 'categoria_uuid': '', 'status': ''
        }
class CatForm(forms.ModelForm):
    class Meta:
        model = CategoriaStock
        fields = ['nombreCategoria','status', 'user_uuid']
        widgets = {
            
        }     
class StocklogForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['producto_uuid', 'stockInicial','StockDescontado', 'StockFinal', 'status','observaciones', 'user_uuid']
        widgets = {
           
            
        }        

