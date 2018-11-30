import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from comun.models import Estados, Restaurantes
from django.urls import reverse

class ProductoStock(models.Model):
    BEBIDAS_LICORES = 'BEB'
    CARNE = 'CAR'
    CONGELADOS = 'CNG'
    DESPENSAS = 'DES'
    FRESCOS_LACTEOS = 'FLA'
    FRUTA = 'FRU'
    OTRO = 'OTR'
    PANADERIA = 'PAN'
    PASTELERIA = 'PAS'
    PESCADOM = 'PES'
    PROD_PREPARADOS = 'PPD'
    VERDURA = 'VER'
    
    CATEGORIA_NOMBRE = {
        (BEBIDAS_LICORES , 'Bebidas y Licores'),
        (CARNE , 'Carnes rojas y blancas'),
        (CONGELADOS , 'Congelados'),
        (DESPENSAS , 'Despensa'),
        (FRESCOS_LACTEOS , 'Frescos y Lacteos'),
        (FRUTA , 'Frutas'),
        (PANADERIA , 'Panaderia'),
        (PASTELERIA , 'Pastaleria'),
        (PESCADOM , 'Pescados y Mariscos'),
        (PROD_PREPARADOS , 'Productos Preparados'),
        (VERDURA , 'Verduras y hortalizas'),
        (OTRO , 'Otros')
    }



    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    codigo = models.CharField(max_length=100, null=True, blank= True)
    porcion = models.IntegerField(default=0, blank=False, null=False)
    unidad_medida = models.CharField(max_length=22, blank=False, default='unidades', null=False)
    no_perecible = models.BooleanField(default= False)
    categoria = models.CharField(max_length= 3, choices= CATEGORIA_NOMBRE, default=OTRO, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    user_uuid = models.CharField(max_length=36)
    stock_disponible = models.IntegerField(null=False, default=0)

    def get_absolute_url(self):
        #return 'stock/registro/nuevo?produto=%s&tipo=init' % self.uuid
        from django.urls import reverse
        return reverse('stock:logCreate', kwargs={'pk': self.uuid, 'accion': 'agregar'})

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    producto_uuid = models.ForeignKey(ProductoStock, on_delete=models.SET_NULL, null=True)
    stock_inicial = models.IntegerField(default=0, null=False, blank=False)
    stock_descontado = models.IntegerField(default=0, null=False, blank=False)
    stock_final = models.IntegerField(default=0, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    fecha_elaboracion = models.DateField(blank=True, null=True)
    fecha_expiracion = models.DateField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    precio_total = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    observaciones = models.CharField(max_length=200, default="", null=True)
    status = models.IntegerField(default=1)
    user_uuid = models.CharField(max_length=36)
   
    def __str__(self):
        return "%s" %(self.uuid)


# producto y categoria  & observaciones
