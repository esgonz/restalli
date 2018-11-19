import uuid
from django.db import models
from comun.models import Estados, Sucursal

class Mesas(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True) #VERIFICAR TIPO DE DATO
    identificador = models.CharField(max_length=20)
    empleado = models.CharField(max_length=50) #VERIFICAR CON ESTEBAN Y SI FALTA HORA INICIO Y FIN
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True) # PREGUNTAR POR QUE
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)