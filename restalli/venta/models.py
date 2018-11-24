import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from comun.models import Estados, Restaurantes
# Create your models here.




class Venta(models.Model):
    DEBITO = 'DEB'
    CREDITO = 'CRE'
    CHEQUE = 'CHE'
    EFECTIVO = 'EFE'

    TIPO_DE_PAGO = {
        (DEBITO, 'DEBITO'),
        (CREDITO, 'CREDITO'),
        (CHEQUE, 'CHEQUE'),
        (EFECTIVO, 'EFECTIVO'),



    }

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tipoPago = models.CharField(max_length= 3, choices= TIPO_DE_PAGO, default=EFECTIVO)
    stockInicial = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados,on_delete=models.SET_NULL, null=True)
    user_uuid = models.CharField(max_length=36)
    def __str__(self):
        return "%s" %(self.uuid)
