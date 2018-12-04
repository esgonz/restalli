from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Pedido, PedidoItem
from .forms import PedidoForm, PedidoUpdateForm
from menu.models import ProductosMenu, CategoriaMenu, ProductosMenuStock
from menu.forms import ProductosMenuForm
from menu.views import MenuList
from mesas.models import Mesas

#from .forms import ProductosMenuForm
# Create your views here.
"""Vistas de menu productos"""
@method_decorator(login_required, name='dispatch')
class PedidoCreation(generic.edit.CreateView):
	model = Pedido
	form_class = PedidoForm
	success_url = reverse_lazy('pedidos:list')
	

	def get_initial(self):
		print("GET INITIAL:")
		total_cart = self.request.session.get('total_cart', [])
		


	def get_context_data(self, **kwargs):
		print("get context:")
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		#try to get cart, if cart doesnt exist, empty list
		cart = self.request.session.get('cart', [])
		# Do stuff with cart
		self.request.session['cart'] = cart
		context['cart_list'] = self.request.session['cart']


		#try to get cart, if cart doesnt exist, empty list
		total_cart = self.request.session.get('total_cart', [])
		# Do stuff with cart
		self.request.session['total_cart'] = total_cart
		context['total_cart'] = self.request.session['total_cart']



		print("CART pedido:")
		print(context['cart_list'])
		return context
	
	def post(self, request, *args, **kwargs):
		
		print("POST create")
		#try to get cart, if cart doesnt exist, empty list
		cart = self.request.session.get('cart', [])
		# Do stuff with cart
		request.session['cart'] = cart


		if 'clear' in request.POST:
			request.session.flush()
		

		elif 'add' in request.POST or 'upde' in request.POST  :
			print("*ADD")
			#si se pulso "agregar" desde la lista de productos disponibles
			uuid_producto = request.POST['uuid']
			productoObject = ProductosMenu.objects.get(uuid=uuid_producto)
			qty_producto = request.POST['qty']

			productoToAdd = {
					"uuid": str(productoObject.uuid),
					"nombre": str(productoObject.nombre),
					"precio": str(productoObject.precio),
					"qty":str(qty_producto)
				} 

			temp_index = 0
			
			#sumar qty si ya existe en el carro
			for index, prod in enumerate(request.session['cart']):
				print("PROD")
				print(prod)

				

				#si existe el id en el carro
				if prod['uuid'] == uuid_producto:
					#prev save object
					producto_temp = prod
					#then delete product
					request.session['cart'].remove(prod)
					
					#change qty and add like a new brand
					if 'add' in request.POST:
						pass
						temp_qty = int(producto_temp['qty']) + int(productoToAdd["qty"])
					else:
						temp_qty = int(productoToAdd["qty"])


					productoToAdd["qty"] = temp_qty
					
				

			if int(productoToAdd['qty'])>0:
				request.session['cart'].append(productoToAdd)
			print(request.session['cart'])

			#recaulcular total
			total_cart = 0
			for index, prod in enumerate(request.session['cart']):
				total_cart = total_cart +  float(float(prod['precio']) * int(prod["qty"]))
				print("total:")
				print(total_cart)	
			#agregar producto al carro seleccion
			
			request.session['total_cart'] = total_cart
		

		elif 'save' in request.POST :
			print("SAVE PEDIDO**")
			
		
		return super(PedidoCreation, self).post(request, *args, **kwargs)

	def form_valid(self, form):
		print("form_valid")
		form.instance.total = self.request.session.get('total_cart', 0)
		pedido = form.save()#commit false doesnt save in the DB, only create in memory
		print(pedido.uuid)
		print(str(pedido.total))
		print (self.request.session['cart'])


		total_cart = 0
		for index, prod in enumerate(self.request.session['cart']):
			print("PROD")
			print(prod)
			print("PROD")
			total_cart = total_cart + float(prod['precio'])
			producto_temp = ProductosMenu.objects.get(uuid = prod['uuid'])

			pedidoItem_to_save = PedidoItem.objects.create(
				productoMenu = producto_temp,
				cantidad = prod['qty'],
				precioVenta = producto_temp.precio,
				subtotal = int(prod['qty'])* producto_temp.precio,
				status = 1,
				pedido_uuid = pedido
			)
			pedidoItem_to_save.save()
		

		#mesa_temp = Mesa.objects.get(uuid = form.instance.mesa.uuid)
		form.instance.mesa.estado = "OCP"
		form.instance.mesa.save()
		print ("END FORM VALID")
		return super(PedidoCreation, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class PedidoCreationMovil(PedidoCreation):
	template_name = "pedidos/pedido_form_movil.html"
	success_url = reverse_lazy('pedidos:mlist')
	model = Pedido
	form_class = PedidoForm
	


@method_decorator(login_required, name='dispatch')
class PedidoDetail(generic.DetailView):
	model = Pedido
	fields = [
		'uuid',
		'numero',
		'sucursal',
		'total',
		'created',
		'updated',
		'deleted',
		'status',
		'estadoPedido'
	]

	def get_context_data(self, **kwargs):
		print("get context:")
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		pedidosItems = PedidoItem.objects.filter(pedido_uuid= self.kwargs['pk']) 
		
		context['items_list'] = []
		for pitem in pedidosItems:

			pitem_to_show = {
				'uuid' : pitem.productoMenu.uuid, 
				'nombre':pitem.productoMenu.nombre,
				'qty': pitem.cantidad,
				'precio': pitem.precioVenta, 
	        }              	
			context['items_list'].append(pitem_to_show)
		#context['items_list']
		return context

@method_decorator(login_required, name='dispatch')
class PedidoDetailMovil(PedidoDetail):
	template_name = "pedidos/pedido_detail_movil.html"

@method_decorator(login_required, name='dispatch')
class PedidoUpdate(generic.UpdateView):
	model = Pedido
	form_class = PedidoUpdateForm
	template_name = "pedidos/pedido_update.html"
	success_url = reverse_lazy('pedidos:list')


	def get_initial(self):
		print("GET INITIAL:")

		if 'estado' in self.request.GET:
			estadoPedido = self.request.GET['estado']

			return {
				'estadoPedido': estadoPedido
	        }


	def get_context_data(self, **kwargs):
		print("get context:")
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		pedidosItems = PedidoItem.objects.filter(pedido_uuid= self.kwargs['pk']) 
		
		context['items_list'] = []
		for pitem in pedidosItems:

			pitem_to_show = {
				'uuid' : pitem.productoMenu.uuid, 
				'nombre':pitem.productoMenu.nombre,
				'qty': pitem.cantidad,
				'precio': pitem.precioVenta, 
	        }              	
			context['items_list'].append(pitem_to_show)
		#context['items_list']
		return context


@method_decorator(login_required, name='dispatch')
class PedidoUpdateMovil(PedidoUpdate):
	template_name = "pedidos/pedido_update_movil.html"

@method_decorator(login_required, name='dispatch')
class PedidoDelete(generic.DeleteView):
	model = Pedido
	#success_url = reverse_lazy('menu:list')

@method_decorator(login_required, name='dispatch')
class PedidoList(generic.ListView):
	model = Pedido

	context_object_name = 'pedidos_list'
	paginate_by = 50

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		#context['categorias_list'] = CategoriaMenu.objects.all()
		return context

	def get_queryset(self):
		#leo el parametro que viene desde get(url)
		filter_val = self.request.GET.get('estado', '')
		if filter_val!='':
			#si el parametro existe, aplico el filtro.
			return Pedido.objects.filter(estadoPedido=filter_val)
		else:
			#si no, devuelvo todos los productos
			return Pedido.objects.all()


@method_decorator(login_required, name='dispatch')    
class PedidoListMovil(PedidoList):
	template_name = "pedidos/pedido_list_movil.html"





"""Menu Oferta """

@method_decorator(login_required, name='dispatch')    	
class MenuOfertList(MenuList):
	model = ProductosMenu
	context_object_name = 'productosMenu_list'
	template_name = 'pedidos/menuOfertas_list.html'
	paginate_by = 100

	

	def post(self, request, *args, **kwargs):
		#try to get cart, if cart doesnt exist, empty list
		cart = self.request.session.get('cart', [])
		# Do stuff with cart
		request.session['cart'] = cart


		if 'clear' in request.POST:
			request.session.flush()
		
		elif 'add' in request.POST or 'upde' in request.POST  :
			print("*ADD")
			#si se pulso "agregar" desde la lista de productos disponibles
			uuid_producto = request.POST['uuid']
			productoObject = ProductosMenu.objects.get(uuid=uuid_producto)
			qty_producto = request.POST['qty']

			productoToAdd = {
					"uuid": str(productoObject.uuid),
					"nombre": str(productoObject.nombre),
					"precio": str(productoObject.precio),
					"qty":str(qty_producto)
				} 

			temp_index = 0
			
			#sumar qty si ya existe en el carro
			for index, prod in enumerate(request.session['cart']):
				print("PROD")
				print(prod)

				

				#si existe el id en el carro
				if prod['uuid'] == uuid_producto:
					#prev save object
					producto_temp = prod
					#then delete product
					request.session['cart'].remove(prod)
					
					#change qty and add like a new brand
					if 'add' in request.POST:
						pass
						temp_qty = int(producto_temp['qty']) + int(productoToAdd["qty"])
					else:
						temp_qty = int(productoToAdd["qty"])


					productoToAdd["qty"] = temp_qty
					
				

			if int(productoToAdd['qty'])>0:
				request.session['cart'].append(productoToAdd)
			print(request.session['cart'])

			#recaulcular total
			total_cart = 0
			for index, prod in enumerate(request.session['cart']):
				total_cart = total_cart +  float(float(prod['precio']) * int(prod["qty"]))
				print("total:")
				print(total_cart)	
			#agregar producto al carro seleccion
			
			request.session['total_cart'] = total_cart
			

		
		return super().get(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		# Add in a QuerySet of all the books
		context['categorias_list'] = CategoriaMenu.objects.all()

		#try to get cart, if cart doesnt exist, empty list
		cart = self.request.session.get('cart', [])
		# Do stuff with cart
		self.request.session['cart'] = cart
		context['cart_list'] = self.request.session['cart']

		#try to get cart, if cart doesnt exist, empty list
		total_cart = self.request.session.get('total_cart', [])
	
		# Do stuff with cart
		self.request.session['total_cart'] = total_cart
		context['total_cart'] = self.request.session['total_cart']


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



"""Menu Oferta Movil """
@method_decorator(login_required, name='dispatch')
class MenuOfertaListMovil(MenuOfertList):
	template_name = 'pedidos/menuOfertas_list_movil.html'
    	
