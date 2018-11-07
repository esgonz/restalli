import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.


class CategoriaMenu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombreCategoria = models.CharField(max_length=95)
    _created = models.DateTimeField(auto_now_add=True)
    _updated= models.DateTimeField(auto_now=True)
    _deleted = models.DateTimeField(auto_now=True)
    _status = models.IntegerField()


class ProductosMenu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombreProducto = models.CharField(max_length=45)
    slugProducto = models.SlugField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    precioOferta = models.DecimalField(max_digits=9, decimal_places=2)
    inicioOferta = models.DateTimeField()
    terminoOferta = models.DateTimeField()
    _created= models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)
    _deleted = models.DateTimeField(auto_now=True)
    _status = models.IntegerField()
    categoria_uuid = models.ForeignKey(CategoriaMenu, on_delete=models.CASCADE)
    productosMenuStock_uuid = models.CharField(max_length=36)
    restaurant_uuid = models.CharField(max_length=36)
    user_uuid = models.CharField(max_length=36)
    def get_absolute_url(self):
            return('producto_detail', (),
                {
                    'slugProducto':self.slugProducto
                })

    def save( self, *args, **kwargs):
        if not self.slugProducto:
            self.slugProducto= slugify(self.nombreProducto)
            super(ProductosMenu, self).save(*args, **kwargs)

class ProductosMenuStock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    stock_uuid = models.CharField(max_length=36)
    productosMenu_uuid = models.ForeignKey(ProductosMenu, on_delete=models.CASCADE)
    porciones = models.IntegerField()


