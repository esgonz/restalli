from django import forms
from .models import Mesas, Reserva

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




class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reserva
        
        fields = [
            'fecha', 
            'cliente_nombre',
            'cliente_numero1', 
            'cliente_numero2',
            'cliente_email',
            'num_personas',
            'comentarios',
            'mesa_uuid'
        ]
        
        widgets = {
            #'identificador' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Mesa 01'}),
        }
        labels = {
            'fecha': 'Fecha y Hora reserva' , 
            'cliente_nombre': 'Nombre Cliente' ,
            'cliente_numero1': 'Telefono contacto' , 
            'cliente_numero2': 'Telefono contacto alternativo' ,
            'cliente_email': 'Email de contacto' ,
            'num_personas': 'Numero de personas' ,
            'comentarios': 'Comentarios' ,
            'mesa_uuid': 'Mesa'
        }

