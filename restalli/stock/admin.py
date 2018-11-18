from django.contrib import admin
from .models import ProductoStock, Stock, CategoriaStock
# Register your models here.

admin.site.register(ProductoStock)
admin.site.register(Stock)
admin.site.register(CategoriaStock)