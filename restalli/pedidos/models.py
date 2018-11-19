import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from menu.models import ProductosMenu, CategoriaMenu
from comun.models import Estados, Restaurantes, Sucursal
# Create your models here.


#Pedido
class Pedido(models.Model):

    PENDIENTE = 'INIT'
    ESPERA = 'WAIT'
    ENTREGADO = 'OK'
    CANCELADO = 'CNCL'
    FINALIZADO = 'FNLZ'
    ESTADO_PEDIDO_CHOICES = (
        (PENDIENTE, 'Pendiente'),
        (ESPERA, 'Espera'),
        (ENTREGADO, 'Entregado'),
        (CANCELADO, 'Cancelado'),
        (FINALIZADO, 'Finalizado'),
    )
    



    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    numero = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    estadoPedido = models.CharField(
        max_length=5,
        choices=ESTADO_PEDIDO_CHOICES,
        default=PENDIENTE,
    )
    user_uuid = models.CharField(max_length=36)
    
    def __str__(self):
        return "%s" % (self.numero)

#Pedido
class PedidoItem(models.Model):

    PENDIENTE = 'INIT'
    ESPERA = 'WAIT'
    ENTREGADO = 'OK'
    CANCELADO = 'CNCL'
    FINALIZADO = 'FNLZ'
    ESTADO_PEDIDO_ITEMS_CHOICES = (
        (PENDIENTE, 'Pendiente'),
        (ESPERA, 'Espera'),
        (ENTREGADO, 'Entregado'),
        (CANCELADO, 'Cancelado'),
        (FINALIZADO, 'Finalizado'),
    )
    



    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    productoMenu = models.ForeignKey(ProductosMenu, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precioVenta = models.DecimalField(max_digits=9, decimal_places=2)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    estadoPedido = models.CharField(
        max_length=5,
        choices=ESTADO_PEDIDO_ITEMS_CHOICES,
        default=PENDIENTE,
    )
    user_uuid = models.CharField(max_length=36)
    
    def __str__(self):
        return "%s" % (self.uuid)




