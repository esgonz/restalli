from django.db import models

# Create your models here.
class stock(models.Model):
    
    title = models.CharField(max_length=200)
    slugStock = models.SlugField(unique=True, max_length=255)
    categoria = models.CharField(max_length=25)
    porciones = models.IntegerField()
    cantidad = models.IntegerField()
    price = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField()
  

 
    def __str__(self):
        return self.title