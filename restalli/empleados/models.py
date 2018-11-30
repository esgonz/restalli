import uuid
from django.db import models
from comun.models import Estados, Personas

class Empleados(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=8) # VERIFICAR
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    personas = models.ForeignKey(Personas, on_delete=models.SET_NULL, null=True)

# ¿FALTA REFERENCIA A PERFIL EMPLEADO?