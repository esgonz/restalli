from django import forms
from .models import ProductoStock, Stock
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class StockForm(forms.ModelForm):



    class Meta:
        model = ProductoStock
        fields = ['nombre', 'codigo','porcion', 'unidad_medida', 
        'no_perecible', 'categoria' ]
        

        labels = {
            'nombre': 'Nombre Producto', 
            'codigo': 'Código', 
            'porcion': 'Porciones por unidad',
            'unidad_medida': 'Und. medida porciones',
            'no_perecible': '¿No perecible?',
            'categoria': 'Categoria'
        } 
class StocklogForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = [
            'producto_uuid', 
            'stock_inicial',
            'stock_descontado', 
            'stock_final', 
            'fecha_elaboracion',
            'fecha_expiracion', 
            'precio_unitario',
            'precio_total',
            'observaciones'

        ]

        labels = {
            'producto_uuid': 'Producto', 
            'stock_inicial': 'Stock Actual', 
            'stock_descontado': 'Nuevo Stock',
            'stock_final': 'Stock Final',
            'fecha_elaboracion': 'Fecha Elaboración',
            'fecha_expiracion': 'Fecha Expiración',
            'precio_unitario': 'Precio unitario compra',
            'precio_total': 'Costo total',
            'observaciones': 'Observaciones'
        } 

        widgets = {
            'observaciones': forms.Textarea(attrs={'cols': 35, 'rows': 10}),
            'fecha_elaboracion': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            'fecha_expiracion' : forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            'stock_inicial' : forms.TextInput(attrs={'readonly':True, 'class': 'form-control'}),
            'stock_final' : forms.TextInput(attrs={'readonly':True, 'class': 'form-control'}),
            'producto_uuid' : forms.Select(attrs={'readonly':True, 'class': 'form-control'}),
            'precio_unitario': forms.TextInput(attrs={ 'type':'number', 'step':'any',  'class': 'form-control'}),
            'stock_descontado' : forms.TextInput(attrs={  'class': 'form-control'}),
            
        }

        
        help_texts = {
            'producto_uuid': 'Producto', 
            'stock_inicial': 'Stock existente', 
            'stock_descontado': 'Cantidad a agregar/descontar',
            'stock_final': 'Stock final luego de aplicar agregar/descontar stock',
            'fecha_elaboracion': 'Fecha Elaboración',
            'fecha_expiracion': 'Fecha Expiración',
            'precio_unitario': 'Precio unitario compra',
            'precio_total': 'Costo total (precio unitario x cantidad)',
            'observaciones': 'Mensaje o registro'
        }
        error_messages = {
            'producto_uuid': {
                'required': "Debe ingresar precio unitario",
            },
            'stock_inicial': {
                'required': "Debe existir un stock previo",
            },
            'stock_descontado': {
                'required': "Debe ingresar una cantidad",
            },
            'stock_final': {
                'required': "Debe existir un stock final",
            },
            'fecha_elaboracion': {
                'required': "Debe ingresar fecha de elaboracion",
            },
            'fecha_expiracion': {
                'required': "Debe ingresar fecha de expiracion",
            },
            'precio_unitario': {
                'required': "Debe ingresar precio unitario",
            },
            'precio_total': {
                'required': "Debe ingresar precio total",
            },
            'observaciones': {
                'required': "Debe ingresar observaciones",
            }
        }


