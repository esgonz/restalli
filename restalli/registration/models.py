from django.db import models
import uuid
from comun.models import Estados

# Create your models here.

class Perfiles(models.Model):

    MANAGER = 'MNG'
    MESERO = 'MSR'
    CAJERO = 'CJA'
    
    PERFIL_CHOICES = (
        (MANAGER, 'Administrador'),
        (MESERO, 'Mesero'),
        (CAJERO, 'Cajero'),
        
    )




    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    avatar = models.ImageField(upload_to='perfiles', null= True, blank= True)
    user = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    perfil = models.CharField(
        max_length=3,
        choices=PERFIL_CHOICES,
        default=MESERO,
    )
    password = models.CharField(max_length=16) # VERIFICAR
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    objects = models.Manager()