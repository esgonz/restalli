import uuid
from django.db import models
from comun.models import Estados, Sucursal

class Mesas(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    identificador = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    pedido = models.CharField(max_length=10)
    empleado = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    inicio = models.CharField(max_length=50)
    termino = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)