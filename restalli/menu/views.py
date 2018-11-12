from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import ProductosMenu, CategoriaMenu, ProductosMenuStock
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'menu/index.html'
	context_object_name = 'latest_productos_list'

	def get_queryset(self):
		"""Return the last 5 published menus"""
		return ProductosMenu.objects.order_by('-_created')[:5]


#def index(request):
	#return HttpResponse ("Hello, world. You're at the menu index.")
	#
#	template = loader.get_template('menu/index.html')
#	context = {}
#	return render(request, template, context)



#def seleccionarStock(request):
	#return HttpResponse("Seleccionar desde el stock de productos,")
#	template = loader.get_template('menu/nuevo.html')
#	context = {}
#	return render(request, template, context)




class CrearView(generic.edit.CreateView):
	model = ProductosMenu
	fields = [
		'nombreProducto',
		'descripcion',
		'precio',
		'_status'
	]
	#template_name = 'menu/nuevo_paso2.html'
#def crear(request):
	#do something
	#return HttpResponse("Crear un nuevo producto Aqui")
#	template = loader.get_template('menu/nuevo_paso2.html')
#	context = {}
#	return render(request, template, context)




class EditarView(generic.DetailView):
	model = ProductosMenu
	#template_name = 'menu/editar.html'
#def editar(request, producto_uuid):
	#do something
	#return HttpResponse("quieres editar el producto %s" % producto_uuid)
#	template = loader.get_template('menu/editar.html')
#	context = {}
#	return render(request, template, context)

#def listar(request):
	#do something
	#return HttpResponse(" Listar Productos Aqui")
#	template = loader.get_template('menu/lista.html')
#	context = {}
#	return render(request, template, context)
