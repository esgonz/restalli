from django.contrib import admin

# Register your models here.
from .models import CategoriaStock, Stock, ProductoStock

admin.site.register(Stock)
admin.site.register(CategoriaStock)
admin.site.register(ProductoStock)