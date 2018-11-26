from django.db import models
import uuid
from comun.models import Estados

# Create your models here.

class Perfiles(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    avatar = models.ImageField(upload_to='perfiles', null= True, blank= True)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=8) # VERIFICAR
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)

    objects = models.Manager()