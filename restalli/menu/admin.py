from django.contrib import admin

# Register your models here.
from .models import ProductosMenu, CategoriaMenu, ProductosMenuStock

admin.site.register(ProductosMenu)
admin.site.register(CategoriaMenu)
admin.site.register(ProductosMenuStock)