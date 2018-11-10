from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
	#return HttpResponse ("Hello, world. You're at the menu index.")
	#
	template = loader.get_template('menu/index.html')
	context = {}
	return render(request, template, context)

def seleccionarStock(request):
	#return HttpResponse("Seleccionar desde el stock de productos,")
	template = loader.get_template('menu/nuevo.html')
	context = {}
	return render(request, template, context)

def crear(request):
	#do something
	#return HttpResponse("Crear un nuevo producto Aqui")
	template = loader.get_template('menu/nuevo_paso2.html')
	context = {}
	return render(request, template, context)


def editar(request, producto_uuid):
	#do something
	#return HttpResponse("quieres editar el producto %s" % producto_uuid)
	template = loader.get_template('menu/editar.html')
	context = {}
	return render(request, template, context)

def listar(request):
	#do something
	#return HttpResponse(" Listar Productos Aqui")
	template = loader.get_template('menu/lista.html')
	context = {}
	return render(request, template, context)
