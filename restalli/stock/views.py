from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.template import loader
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import ProductoStock, Stock, CategoriaStock
from .forms import StockForm, CatForm, StocklogForm

# index 
class IndexView(generic.ListView):
        template_name = 'stock/Stock.html'
        context_object_name = 'latest_stock_list'

class StaffRequiredMixin(object):
  @method_decorator(staff_member_required)  
  def dispatch(self, request, *args, **kwargs):
       if not request.user.is_staff:
        return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)   

# Create your views here.aa
class stockListView(generic.ListView):
    model = ProductoStock
    paginate_by = 3
    context_object_name = 'productoStock_list'


    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
          context = super().get_context_data(**kwargs)
            # Add in a QuerySet of all the books
          context['categorias_list'] = CategoriaStock.objects.all()
          return context
    def get_queryset(self):
            #leo el parametro que viene desde get(url)
            filter_val = self.request.GET.get('categoria', '')
            if filter_val!='':
                #si el parametro existe, aplico el filtro.
                return ProductoStock.objects.filter(categoria_uuid=filter_val)
            else:
                #si no, devuelvo todos los productos
                return ProductoStock.objects.all()
        


class stockDetailView(generic.DetailView):
    model = ProductoStock
#success_url = reverse_lazy('stock:list')

@method_decorator(staff_member_required, name='dispatch')
class stockCreate(generic.CreateView):
    model = ProductoStock
    form_class = StockForm
    success_url = reverse_lazy('stock:Create')

    #def form_valid(self, form):
    #  form.instance.ProductoStock = self.request.categoria_uuid
    #  return redirect('/')

class stockUpdate(generic.UpdateView):
    model = ProductoStock
    form_class = StockForm
    #template_name_suffix = '_update_form' 
    success_url = reverse_lazy('stock:list')
    #def get_success_url(self):
     #   return reverse_lazy('stock:list', args=[self.object.uuid()]) + '?ok'
    #def get_object(self):
     #   return ProductoStock.objects.get(uuid=self.kwargs.get("uuid"))
    #def get_success_url(self):
     #   return reverse_lazy('stock:list', args=[self.uuid.UUID(), ])

class stockDelete(generic.DeleteView):
    model = ProductoStock
    success_url = reverse_lazy('stock:list')

#Stock Logico

class stocklogListView(generic.ListView):
    model = Stock

class stocklogDetailView(generic.DetailView):
    model = Stock

class stocklogCreate(generic.CreateView):
    model = Stock
    form_class = StocklogForm
    success_url = reverse_lazy('stock:list')

class stocklogUpdate(generic.UpdateView):
    model = Stock
    form_class = StocklogForm
    success_url = reverse_lazy('stock:list')

    #template_name_suffix = '_update_form' 

   # def get_success_url(self):
       # return reverse_lazy('stockLog:list', args=[self.object.uuid]) + '?ok'

class stocklogDelete(generic.DeleteView):
    model = Stock
    success_url = reverse_lazy('stocklog:list')


#categorias del stock
class CategoriaCreate(generic.CreateView):
        model = CategoriaStock
        form_class = CatForm
        
        success_url = reverse_lazy('stock:catList')

class CategoriaDetail(generic.DetailView):
        model = CategoriaStock

class CategoriaUpdate(generic.UpdateView):
        model = CategoriaStock
        form_class = CatForm
        success_url = reverse_lazy('stock:catList')
class CategoriaDelete(generic.DeleteView):
        model = CategoriaStock
        success_url = reverse_lazy('stock:catList')

class CategoriaList(generic.ListView):
        model = CategoriaStock
        


