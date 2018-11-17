from django.contrib import admin

# Register your models here.
from .models import Stock, ProductoStock, CategoriaStock

admin.site.register(Stock)
admin.site.register(ProductoStock)
admin.site.register(CategoriaStock)