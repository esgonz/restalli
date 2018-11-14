import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from stock.models import CategoriaStock, ProductoStock, Stock
# Create your models here.


class CategoriaMenu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombreCategoria = models.CharField(max_length=95)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField()



class ProductosMenuStock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    productoStock_uuid = models.ManyToManyField(ProductoStock)
    porciones = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)

#oferta tabla aparte
class ProductosMenu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombreProducto = models.CharField(max_length=45)
    slugProducto = models.SlugField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField()
    categoria_uuid = models.ForeignKey(CategoriaMenu, on_delete=models.CASCADE)
    productoStock_uuid = models.ForeignKey(ProductosMenuStock, on_delete=models.CASCADE)
    restaurant_uuid = models.CharField(max_length=36)
    user_uuid = models.CharField(max_length=36)
    def get_absolute_url(self):
            return('producto_detail', (),
                {
                    'slugProducto':self.slugProducto,
                    'camp2': self.categoria
                })

    def save( self, *args, **kwargs):
        if not self.slugProducto:
            self.slugProducto= slugify(self.nombreProducto)
            super(ProductosMenu, self).save(*args, **kwargs)




class ofertas(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique = True)
    precio = models.DecimalField(max_digits = 9, decimal_places = 2)
    producto = models.ForeignKey(ProductosMenu, on_delete = models.CASCADE)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField()


