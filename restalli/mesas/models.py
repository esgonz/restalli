import uuid
from django.db import models
from comun.models import Estados, Sucursal

class Mesas(models.Model):


    LIBRE = 'FRE'
    OCUPADA = 'OCP'
    RESERVA = 'RSV'
    ESTADO_MESA_CHOICES = (
        (LIBRE, 'Libre'),
        (OCUPADA, 'Ocupada'),
        (RESERVA, 'Reservada'),    
    )


    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    identificador = models.CharField(max_length=20, null=False, blank=False)
    empleado = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    estado = models.CharField(
        max_length=3,
        choices=ESTADO_MESA_CHOICES,
        default=LIBRE,
    )
    def __str__(self):
        return "%s" % (self.identificador)
class Reserva(models.Model):


    def ids():
        no = Reserva.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    numero = models.IntegerField(('Code'), default=ids, unique=True, editable=False)
    fecha =  models.DateTimeField(blank=True, null=True)
    cliente_nombre = models.CharField(max_length=200, blank=False, null=False)
    cliente_numero1 = models.CharField(max_length=30, blank=False, null=False)
    cliente_numero2 = models.CharField(max_length=30, blank=True, null=True)
    cliente_email = models.EmailField(max_length=100, blank=True, null=True)
    num_personas = models.IntegerField(default=1)
    comentarios = models.CharField(max_length=300, blank=True, null=True)
    empleado = models.CharField(max_length=50)
    mesa_uuid = models.ForeignKey(Mesas, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "%s" % (self.numero)



