import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from comun.models import Estados, Restaurantes

class CategoriaStock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombreCategoria = models.CharField(max_length=95)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados,on_delete=models.SET_NULL, null=True)
    user_uuid = models.CharField(max_length=36)
    def __str__(self):
        return self.nombreCategoria


class ProductoStock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombreProducto = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    porcion = models.IntegerField()
    unidadMedida = models.CharField(max_length=22)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    fechaElaboracion = models.DateTimeField()
    fechaExpiracion = models.DateTimeField()
    categoria_uuid = models.ForeignKey(CategoriaStock, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados,on_delete=models.SET_NULL, null=True)
    user_uuid = models.CharField(max_length=36)

    def get_absolute_url(self):
        return reversed('detail', kwargs={'pk': self.uuid})

    def __str__(self):
        return self.nombreProducto

class Stock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    producto_uuid = models.ForeignKey(ProductoStock, on_delete=models.SET_NULL, null=True)
    stockInicial = models.IntegerField()
    StockDescontado = models.IntegerField()
    StockFinal = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    observaciones = models.CharField(max_length=200, default="", null=True)
    status = models.IntegerField()
    user_uuid = models.CharField(max_length=36)
    def __str__(self):
        return "%s" %(self.uuid)
# producto y categoria  & observaciones
