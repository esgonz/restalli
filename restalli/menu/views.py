from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	#return HttpResponse ("Hello, world. You're at the menu index.")
	context = {}
	return render(request, 'menu/index.html', context)

def seleccionarStock(request):
	#return HttpResponse("Seleccionar desde el stock de productos,")
	context = {}
	return render(request, 'menu/nuevo.html', context)

def crear(request):
	#do something
	#return HttpResponse("Crear un nuevo producto Aqui")
	context = {}
	return render(request, 'menu/nuevo_paso2.html', context)


def editar(request, producto_uuid):
	#do something
	#return HttpResponse("quieres editar el producto %s" % producto_uuid)
	context = {}
	return render(request, 'menu/editar.html', context)

def listar(request):
	#do something
	#return HttpResponse(" Listar Productos Aqui")
	context = {}
	return render(request, 'menu/lista.html', context)
