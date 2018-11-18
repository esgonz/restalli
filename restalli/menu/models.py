import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from stock.models import CategoriaStock, ProductoStock, Stock
from comun.models import Estados, Restaurantes
# Create your models here.


class CategoriaMenu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombre = models.CharField(max_length=95)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return "%s" % (self.nombre)



#oferta tabla aparte
class ProductosMenu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombre = models.CharField(max_length=45)
    slug = models.SlugField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='productos_menu', blank=True, default ="nodisponible.png")
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    categoria_uuid = models.ForeignKey(CategoriaMenu, on_delete=models.SET_NULL, null=True)
    restaurant_uuid = models.ForeignKey(Restaurantes, on_delete=models.SET_NULL, null=True)
    user_uuid = models.CharField(max_length=36)
    def get_absolute_url(self):
            return('producto_detail', (),
                {
                    'slug':self.slug,
                    'categoria': self.categoria_uuid
                })

    def __str__(self):
        return "%s" % (self.nombre)



class ProductosMenuStock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    productoStock_uuid = models.ForeignKey(ProductoStock, on_delete=models.CASCADE)
    productosMenu_uuid = models.ForeignKey(ProductosMenu, on_delete=models.CASCADE)
    porciones = models.IntegerField()
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)

    


class ofertas(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique = True)
    precio = models.DecimalField(max_digits = 9, decimal_places = 2)
    producto = models.ForeignKey(ProductosMenu, on_delete = models.CASCADE)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)


