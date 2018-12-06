from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ProductosMenu, CategoriaMenu, ProductosMenuStock
from .forms import ProductosMenuForm

from stock.models import ProductoStock

"""Vistas de menu productos"""
@method_decorator(login_required, name='dispatch')
class MenuCreation(generic.edit.CreateView):
	model = ProductosMenu
	"""fields = [
		'nombreProducto',
		'descripcion',
		'precio',
		'status',
		'categoria_uuid',
		'restaurant_uuid',
		'user_uuid'
	]"""
	form_class = ProductosMenuForm
	#success_url = reverse_lazy('menu:list')

@method_decorator(login_required, name='dispatch')
class MenuDetail(generic.DetailView):
	model = ProductosMenu
	#template_name = 'menu/editar.html'
	#
@method_decorator(login_required, name='dispatch')
class MenuUpdate(generic.UpdateView):
	model = ProductosMenu
	form_class = ProductosMenuForm
	success_url = reverse_lazy('menu:list')
	template_name = 'menu/productosMenu_edit.html'

@method_decorator(login_required, name='dispatch')
class MenuDelete(generic.DeleteView):
	model = ProductosMenu
	success_url = reverse_lazy('menu:list')

@method_decorator(login_required, name='dispatch')
class MenuList(generic.ListView):
	model = ProductosMenu
	paginate_by = 50
	context_object_name = 'productosMenu_list'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# get all categories
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
    	



"""Vistas de categorias"""

@method_decorator(login_required, name='dispatch')
class CategoriaCreation(generic.edit.CreateView):
	model = CategoriaMenu
	fields = [
		'nombre',
	]
	success_url = reverse_lazy('menu:catList')
@method_decorator(login_required, name='dispatch')
class CategoriaDetail(generic.DetailView):
	model = CategoriaMenu
@method_decorator(login_required, name='dispatch')
class CategoriaUpdate(generic.UpdateView):
	model = CategoriaMenu
	fields = [
		'nombre',
		'status'
	]
	success_url = reverse_lazy('menu:catList')
@method_decorator(login_required, name='dispatch')
class CategoriaDelete(generic.DeleteView):
	model = CategoriaMenu
	success_url = reverse_lazy('menu:catList')
@method_decorator(login_required, name='dispatch')
class CategoriaList(generic.ListView):
	model = CategoriaMenu






"""Vistas del menu stock"""
@method_decorator(login_required, name='dispatch')
class ProductosMenuStockCreation(generic.edit.CreateView):
	model = ProductosMenuStock
	fields = [
		'productoStock_uuid',
    	'porciones',
    	'status'
	]
@method_decorator(login_required, name='dispatch')
class ProductosMenuStockDetail(generic.DetailView):
	model = ProductosMenu
@method_decorator(login_required, name='dispatch')
class ProductosMenuStockUpdate(generic.UpdateView):
	model = ProductosMenuStock
	fields = [
		'productoStock_uuid',
    	'porciones',
    	'status'
	]
	success_url = reverse_lazy('menu:catList')
@method_decorator(login_required, name='dispatch')
class ProductosMenuStockDelete(generic.DeleteView):
	model = ProductosMenuStock
	success_url = reverse_lazy('menu:catList')



@method_decorator(login_required, name='dispatch')
class ProductosMenuStockList(generic.ListView):
	model = ProductoStock
	template_name ='menu/productoStock_selection_list.html'
	context_object_name = 'productoStock_list'
	paginate_by = 50


	def get_queryset(self):
		#leo el parametro que viene desde get(url)
		filter_val = self.request.GET.get('categoria', '')
		if filter_val!='':
			#si el parametro existe, aplico el filtro.
			return ProductoStock.objects.filter(categoria=filter_val)
		else:
			#si no, devuelvo todos los productos
			return ProductoStock.objects.all()


	def post(self, request, *args, **kwargs):
		
		print("-POST")

		self.productoMenu_uuid = kwargs.get("producto")

		#busco el producto/platillo que estoy actualizando
		productoMenu = ProductosMenu.objects.get(uuid= kwargs.get("producto"))
		print("PROD MENU")
		print(productoMenu.uuid)
		print(productoMenu.nombre)


		#selecciono la seleccion en cookies, si no creo 1 vacia
		seleccion = self.request.session.get('seleccion', [])
		# Do stuff with cart
		request.session['seleccion'] = seleccion

		#controlando carro de seleccion
		#
		if 'clear' in request.POST:
			print("*CLEAR")
			#request.session.flush()
		

		elif 'add' in request.POST or 'upde' in request.POST  :
			print("*ADD")
			#si se pulso "agregar" desde la lista de productos disponibles
			uuid_producto = request.POST['uuid']
			productoObject = ProductoStock.objects.get(uuid=uuid_producto)
			qty_producto = request.POST['qty']

			productoToAdd = {
					"obj_uuid": None,
					"uuid": str(productoObject.uuid),
					"nombre": str(productoObject.nombre),
					"qty":str(qty_producto)
				} 

			temp_index = 0
			
			#sumar qty si ya existe en el carro
			for index, prod in enumerate(request.session['seleccion']):
				print("PROD")
				print(prod)
				#si existe el id en el carro
				if prod['uuid'] == uuid_producto:
					#prev save object
					producto_temp = prod
					#then delete product
					request.session['seleccion'].remove(prod)
					
					#change qty and add like a new brand
					if 'add' in request.POST:
						pass
						temp_qty = int(producto_temp['qty']) + int(productoToAdd["qty"])
					else:
						temp_qty = int(productoToAdd["qty"])

					productoToAdd["qty"] = temp_qty
					break

			#agregar producto al carro seleccion
			request.session['seleccion'].append(productoToAdd)
			print(request.session['seleccion'])
		
		elif 'save' in request.POST:
			
			print("*SAVE")
			for index, prod in enumerate(request.session['seleccion']):
				
				productoStock_aux = ProductoStock.objects.get(uuid= prod['uuid'])
				print(productoStock_aux.uuid)
				print(productoStock_aux.nombre)
				print(prod['obj_uuid'])

				if prod['obj_uuid'] != None:
					print("update product :")
					print(productoStock_aux.nombre)
					productoMenu_to_save = ProductosMenuStock.objects.get(uuid= prod['obj_uuid'])
					productoMenu_to_save.porciones = int(prod['qty'])
				else:
					print("create product :")
					print(productoStock_aux.nombre)
					productoMenu_to_save = ProductosMenuStock.objects.create(
						productoStock_uuid = productoStock_aux,
						productosMenu_uuid = productoMenu,
						porciones = int(prod['qty']),
					)
				#print(productoMenu_to_save)
				productoMenu_to_save.save()

		else:
			pass
			#request.session.flush()


		return super().get(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		print("--CONTEXT DATA:")
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		#try to get cart, if cart doesnt exist, empty list
		seleccion = self.request.session.get('seleccion', [])
		# Do stuff with cart
		self.request.session['seleccion'] = seleccion
		context['seleccion_list'] = self.request.session['seleccion']
		context['producto'] = ProductosMenu.objects.get(uuid= self.productoMenu_uuid)
		context['categorias_list'] = ProductoStock.CATEGORIA_NOMBRE
		print("NUEVO seleccion:")
		print(context['seleccion_list'])
		return context


	def get(self, request, *args, **kwargs):
		print("---GET")
		#self.object = self.get_object(queryset=Publisher.objects.all())
		self.productoMenu_uuid = kwargs.get("producto")
		self.updateSelected = request.GET.get("update")
		print("update ?")
		print(self.updateSelected)
		print(self.productoMenu_uuid )
		#if we are editing selected stock producots
		if self.updateSelected and 'add' not in request.POST:
			print("updateSelected TRUE")
			#request.session.flush()
			selectedProducts_list = ProductosMenuStock.objects.filter(productosMenu_uuid = self.productoMenu_uuid)
			seleccion = []
			request.session['seleccion'] = seleccion
			print(len(selectedProducts_list))
			print(selectedProducts_list)
			for prod in selectedProducts_list:
				print("PROD")
				print(prod)
				print(prod.productoStock_uuid.uuid)
				print(prod.productoStock_uuid.nombre)
				print(prod.porciones)
				print("---")
				productoToAdd = {
					"obj_uuid": str(prod.uuid),
					"uuid": str(prod.productoStock_uuid.uuid),
					"nombre": str(prod.productoStock_uuid.nombre),
					"qty":str(prod.porciones)
				} 

				request.session['seleccion'].append(productoToAdd)
		else:
			print("updateSelected FALSE")
			#request.session.flush()

		return super().get(request, *args, **kwargs)



