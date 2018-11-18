from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic



from .models import ProductosMenu, CategoriaMenu, ProductosMenuStock
from .forms import ProductosMenuForm

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'menu/index.html'
	context_object_name = 'latest_productos_list'

	def get_queryset(self):
		"""Return the last 5 published menus"""
		return ProductosMenu.objects.order_by('-created')[:5]


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


	#template_name = 'menu/nuevo_paso2.html'
#def crear(request):
	#do something
	#return HttpResponse("Crear un nuevo producto Aqui")
#	template = loader.get_template('menu/nuevo_paso2.html')
#	context = {}
#	return render(request, template, context)




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
	paginate_by = 1

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['categorias_list'] = CategoriaMenu.objects.all()
		return context

	def get_queryset(self):
		filter_val = self.request.GET.get('categoria', '')
		if filter_val!='':
			return ProductosMenu.objects.filter(categoria_uuid=filter_val)
		else:
			return ProductosMenu.objects.all()
    	


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



