from django.contrib import admin

# Register your models here.
from .models import Estados, Restaurantes, Sucursal

admin.site.register(Estados)
admin.site.register(Restaurantes)
admin.site.register(Sucursal)