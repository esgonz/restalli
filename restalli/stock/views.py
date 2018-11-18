from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.template import loader
from .models import ProductoStock, Stock, CategoriaStock
from .forms import StockForm, CatForm, StocklogForm

# index 
class IndexView(generic.ListView):
        template_name = 'stock/Stock.html'
        context_object_name = 'latest_stock_list'

#class StaffRequiredMixin(object):
 # def dispatch(self, request, *args, **kwargs):
  #      if not request.user.is_staff:
   #         return redirect(reverse_lazy('admin:login'))
    #    return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)   

# Create your views here.aa
class stockListView(generic.ListView):
    model = ProductoStock

class stockDetailView(generic.DetailView):
    model = ProductoStock

class stockCreate(generic.CreateView):
    model = ProductoStock
    form_class = StockForm
    success_url = reverse_lazy('stock:list')

class stockUpdate(generic.UpdateView):
    model = ProductoStock
    form_class = StockForm
    template_name_suffix = '_update_form' 

    def get_success_url(self):
        return reverse_lazy('stock:list', args=[self.object.uuid]) + '?ok'

class stockDelete(generic.DeleteView):
    model = ProductoStock
    success_url = reverse_lazy('list:list')

#Stock Logico

class stocklogListView(generic.ListView):
    model = Stock

class stocklogDetailView(generic.DetailView):
    model = Stock

class stocklogCreate(generic.CreateView):
    model = Stock
    form_class = StocklogForm
    success_url = reverse_lazy('stockLog:list')

class stocklogUpdate(generic.UpdateView):
    model = Stock
    form_class = StocklogForm
    template_name_suffix = '_update_form' 

    def get_success_url(self):
        return reverse_lazy('stockLog:list', args=[self.object.uuid]) + '?ok'

class stocklogDelete(generic.DeleteView):
    model = Stock
    success_url = reverse_lazy('list:list')


#categorias del stock
class CategoriaCreate(generic.CreateView):
        model = CategoriaStock
        form_class = CatForm
        success_url = reverse_lazy('stock:catList')

class CategoriaDetailView(generic.DetailView):
        model = CategoriaStock

class CategoriaUpdate(generic.UpdateView):
        model = CategoriaStock
        form_class = CatForm
        success_url = reverse_lazy('stock:catList')
class CategoriaDeleteView(generic.DeleteView):
        model = CategoriaStock
        success_url = reverse_lazy('stock:catList')

class CategoriaListView(generic.ListView):
        model = CategoriaStock


