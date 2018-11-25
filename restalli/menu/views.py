from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import ProductosMenu, CategoriaMenu, ProductosMenuStock
from .forms import ProductosMenuForm

from stock.models import ProductoStock

"""Vistas de menu productos"""

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


class MenuDetail(generic.DetailView):
	model = ProductosMenu
	#template_name = 'menu/editar.html'
	#

class MenuUpdate(generic.UpdateView):
	model = ProductosMenu
	form_class = ProductosMenuForm
	success_url = reverse_lazy('menu:list')

class MenuDelete(generic.DeleteView):
	model = ProductosMenu
	success_url = reverse_lazy('menu:list')

class MenuList(generic.ListView):
	model = ProductosMenu
	paginate_by = 10
	context_object_name = 'productosMenu_list'

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
    	



"""Vistas de categorias"""


class CategoriaCreation(generic.edit.CreateView):
	model = CategoriaMenu
	fields = [
		'nombre',
		'status'
	]
	success_url = reverse_lazy('menu:catList')

class CategoriaDetail(generic.DetailView):
	model = CategoriaMenu

class CategoriaUpdate(generic.UpdateView):
	model = CategoriaMenu
	fields = [
		'nombre',
		'status'
	]
	success_url = reverse_lazy('menu:catList')

class CategoriaDelete(generic.DeleteView):
	model = CategoriaMenu
	success_url = reverse_lazy('menu:catList')

class CategoriaList(generic.ListView):
	model = CategoriaMenu






"""Vistas del menu stock"""

class ProductosMenuStockCreation(generic.edit.CreateView):
	model = ProductosMenuStock
	fields = [
		'productoStock_uuid',
    	'porciones',
    	'status'
	]

class ProductosMenuStockDetail(generic.DetailView):
	model = ProductosMenu

class ProductosMenuStockUpdate(generic.UpdateView):
	model = ProductosMenuStock
	fields = [
		'productoStock_uuid',
    	'porciones',
    	'status'
	]
	success_url = reverse_lazy('menu:catList')

class ProductosMenuStockDelete(generic.DeleteView):
	model = ProductosMenuStock
	success_url = reverse_lazy('menu:catList')




class ProductosMenuStockList(generic.ListView):
	model = ProductoStock
	template_name ='menu/productoStock_selection_list.html'
	context_object_name = 'productoStock_list'
	paginate_by = 5


	def post(self, request, *args, **kwargs):
		
		print("POST ProductosMenuStockList")

		self.productoMenu_uuid = kwargs.get("producto")
		productoMenu = ProductosMenu.objects.get(uuid= kwargs.get("producto"))
		print("PROD MENU")
		print(productoMenu.uuid)
		print(productoMenu.nombre)


		#try to get cart, if cart doesnt exist, empty list
		seleccion = self.request.session.get('seleccion', [])
		# Do stuff with cart
		request.session['seleccion'] = seleccion


		if 'clear' in request.POST:
			request.session.flush()
		elif 'add' in request.POST:
			
			nombre_producto = request.POST['nombre']
			uuid_producto = request.POST['uuid']
			qty_porciones = request.POST['porciones']

			productoStock_to_add = {
					"nombre": str(nombre_producto),
					"uuid": str(uuid_producto),
					"porciones": str(qty_porciones),
				} 
			request.session['seleccion'].append(productoStock_to_add)
			print(request.session['seleccion'])
		elif 'save' in request.POST:
			print("SAVE***")
			for index, prod in enumerate(request.session['seleccion']):
				
				productoStock_aux = ProductoStock.objects.get(uuid= prod['uuid'])
				print(productoStock_aux.uuid)
				print(productoStock_aux.nombre)
				productoMenu_to_save = ProductosMenuStock.objects.create(
					productoStock_uuid = productoStock_aux,
					productosMenu_uuid = productoMenu,
					porciones = int(prod['porciones']),
					)
				#print(productoMenu_to_save)
				#productoMenu_to_save.save()



		return super().get(request, *args, **kwargs)


	def get(self, request, *args, **kwargs):
		#self.object = self.get_object(queryset=Publisher.objects.all())
		self.productoMenu_uuid = kwargs.get("producto")
		return super().get(request, *args, **kwargs)


	def get_context_data(self, **kwargs):
		print("NUEVO LIST CART:")
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		#try to get cart, if cart doesnt exist, empty list
		seleccion = self.request.session.get('seleccion', [])
		# Do stuff with cart
		self.request.session['seleccion'] = seleccion
		context['seleccion_list'] = self.request.session['seleccion']
		context['producto'] = ProductosMenu.objects.get(uuid= self.productoMenu_uuid)


		print("NUEVO seleccion:")
		print(context['seleccion_list'])
		return context


