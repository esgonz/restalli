from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import ProductosMenu, CategoriaMenu, ProductosMenuStock
from .forms import ProductosMenuForm

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
	success_url = reverse_lazy('menu:list')


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
	model = ProductosMenuStock



