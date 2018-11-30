import uuid
from django.db import models

# Create your models here.

class Estados(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	estado = models.CharField(max_length=95)
	created = models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)
	deleted = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return "%s" % (self.estado)



class Restaurantes(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	nombre = models.CharField(max_length=100)
	razonSocial = models.CharField(max_length=150)
	rut = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)
	deleted = models.DateTimeField(auto_now=True)
	status = models.IntegerField(default=1)
	
	def __str__(self):
		return "%s" % (self.nombre)

class Sucursal(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=250)
	comuna = models.CharField(max_length=120)
	ciudad = models.CharField(max_length=120)
	telefono = models.CharField(max_length=15)
	created = models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)
	deleted = models.DateTimeField(auto_now=True)
	status = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
	restaurante_uuid = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)

	def __str__(self):
		return "%s" % (self.nombre)


class Personas(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	nombres = models.CharField(max_length=50)
	apellidoPaterno = models.CharField(max_length=50)
	apellidoMaterno = models.CharField(max_length=50)
	sexo = models.CharField(max_length=1) # DEFINIR LARGO
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=15)
	created = models.DateTimeField(auto_now_add=True)
	updated= models.DateTimeField(auto_now=True)
	deleted = models.DateTimeField(auto_now=True)
	status = models.IntegerField(default=1)
	restaurante_uuid = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)

	def __str__(self):
		return "%s" % (self.nombre)
