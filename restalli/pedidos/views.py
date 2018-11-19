from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Pedido
from menu.models import ProductosMenu, CategoriaMenu, ProductosMenuStock
from menu.forms import ProductosMenuForm
from menu.views import MenuList

#from .forms import ProductosMenuForm
# Create your views here.
"""Vistas de menu productos"""

class PedidoCreation(generic.edit.CreateView):
	model = Pedido
	"""fields = [
		'nombreProducto',
		'descripcion',
		'precio',
		'status',
		'categoria_uuid',
		'restaurant_uuid',
		'user_uuid'
	]"""
	#form_class = ProductosMenuForm
	#success_url = reverse_lazy('menu:list')


class PedidoDetail(generic.DetailView):
	model = Pedido
	#template_name = 'menu/editar.html'
	#

class PedidoUpdate(generic.UpdateView):
	model = Pedido
	#form_class = ProductosMenuForm
	#success_url = reverse_lazy('menu:list')

class PedidoDelete(generic.DeleteView):
	model = Pedido
	#success_url = reverse_lazy('menu:list')

class PedidoList(generic.ListView):
	model = Pedido
	context_object_name = 'pedidos_list'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		#context['categorias_list'] = CategoriaMenu.objects.all()
		return context

	def get_queryset(self):
		#leo el parametro que viene desde get(url)
		filter_val = self.request.GET.get('categoria', '')
		if filter_val!='':
			#si el parametro existe, aplico el filtro.
			return Pedido.objects.filter(numero=filter_val)
		else:
			#si no, devuelvo todos los productos
			return Pedido.objects.all()
    	
class MenuOfertList(MenuList):
	model = ProductosMenu
	context_object_name = 'productos_list'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		# Add in a QuerySet of all the books
		context['categorias_list'] = CategoriaMenu.objects.all()
		return context

	def get_queryset(self):
		#leo el parametro que viene desde get(url)
		filter_val = self.request.GET.get('categoria', '')
		if filter_val!='':
			#si el parametro existe, aplico el filtro.
			return ProductosMenu.objects.filter(categoria_uuid=filter_val)
		else:
			#si no, devuelvo todos los productos
			return ProductosMenu.objects.all()
    	
