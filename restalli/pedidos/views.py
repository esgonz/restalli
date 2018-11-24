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
	context_object_name = 'productosMenu_list'
	template_name = 'pedidos/pedido_list.html'
	paginate_by = 10

	

	def post(self, request, *args, **kwargs):
		cart = self.request.session.get('cart', [])
		# Do stuff with cart
		request.session['cart'] = cart
		


		"""
			{
			   'A': 1,
			   'B': 2,
			   'C': 3,
			}
		"""
		uuid_producto = request.POST['uuid']
		productoObject = ProductosMenu.objects.get(uuid=uuid_producto)
		qty_producto = request.POST['qty']

		productoToAdd = {
			"uuid": str(productoObject.uuid),
			"nombre": str(productoObject.nombre),
			"precio": str(productoObject.precio),
			"qty":str(qty_producto)
		} 
		


		# Set a session value
		request.session['cart'].update(productoToAdd)

		if 'accept' in request.POST:
			# do acceptable stuff
			pass
		elif 'reject' in request.POST:
			# do rejectable stuff
			pass
		print(request.session['cart'])
		return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		# Add in a QuerySet of all the books
		context['categorias_list'] = CategoriaMenu.objects.all()

		context['cart_list'] = self.request.session['cart']

		print("LIST CART:")
		print(context['cart_list'])
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
    	
