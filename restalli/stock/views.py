from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.template import loader
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ProductoStock, Stock
from .forms import StockForm, StocklogForm


# index 
@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    context_object_name = 'latest_stock_list'

class StaffRequiredMixin(object):
  @method_decorator(staff_member_required)  
  def dispatch(self, request, *args, **kwargs):
       if not request.user.is_staff:
        return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)   

# Create your views here.aa
@method_decorator(login_required, name='dispatch')
class stockListView(generic.ListView):
    model = ProductoStock
    paginate_by = 100
    context_object_name = 'productostock_list'


    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
          context = super().get_context_data(**kwargs)
            # Add in a QuerySet of all the books
          return context
    def get_queryset(self):
            #leo el parametro que viene desde get(url)
            filter_val = self.request.GET.get('categoria', '')
            if filter_val!='':
                #si el parametro existe, aplico el filtro.
                return ProductoStock.objects.filter(categoria=filter_val, status = 1)
            else:
                #si no, devuelvo todos los productos
                return ProductoStock.objects.filter( status = 1)
        

@method_decorator(login_required, name='dispatch')
class stockDetailView(generic.DetailView):
    model = ProductoStock
#success_url = reverse_lazy('stock:list')

@method_decorator(login_required, name='dispatch')
class stockCreate(generic.CreateView):
    model = ProductoStock
    form_class = StockForm
    #success_url = reverse_lazy('stock:create')

    #def form_valid(self, form):
    #  form.instance.ProductoStock = self.request.categoria_uuid
    #  return redirect('/')
@method_decorator(login_required, name='dispatch')
class stockUpdate(generic.UpdateView):
    model = ProductoStock
    form_class = StockForm
    template_name = 'stock/productostock_update.html'
    #template_name_suffix = '_update_form' 
    success_url = reverse_lazy('stock:list')
    #def get_success_url(self):
     #   return reverse_lazy('stock:list', args=[self.object.uuid()]) + '?ok'
    #def get_object(self):
     #   return ProductoStock.objects.get(uuid=self.kwargs.get("uuid"))
    #def get_success_url(self):
     #   return reverse_lazy('stock:list', args=[self.uuid.UUID(), ])
@method_decorator(login_required, name='dispatch')
class stockDelete(generic.DeleteView):
    model = ProductoStock
    success_url = reverse_lazy('stock:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())

#Stock Logico

@method_decorator(login_required, name='dispatch')
class stocklogListView(generic.ListView):
    model = Stock

@method_decorator(login_required, name='dispatch')
class stocklogDetailView(generic.DetailView):
    model = Stock

@method_decorator(login_required, name='dispatch')
class stocklogCreate(generic.CreateView):
    model = Stock
    form_class = StocklogForm
    success_url = reverse_lazy('stock:list')

    def get_initial(self):
        print("GET INITIAL:")

        producto = ProductoStock.objects.get(uuid= self.kwargs['pk'])

        return {
            'producto_uuid': self.kwargs['pk'],
            'stock_inicial': producto.stock_disponible,
            'stock_final' :  producto.stock_disponible,
            'fecha_elaboracion': None,
            'fecha_expiracion': None,
            'precio_unitario': 0,
            'precio_total': 0
        }

    def get(self, request, *args, **kwargs):

        
        #self.object = self.get_object(queryset=Publisher.objects.all())
        self.producto_uuid = kwargs.get("pk")
        return super().get(request, *args, **kwargs)

    """def post(self, request, *args, **kwargs):
        print("POST:")
        
        #self.object = self.get_object(queryset=Publisher.objects.all())
        self.producto_uuid = kwargs.get("pk")
        return super(stocklogCreate, self).get(request, *args, **kwargs)"""
    
    def form_valid(self, form):
        accion =self.kwargs['accion']
        if accion == 'descontar':
            form.instance.stock_final = (form.instance.stock_inicial)-(form.instance.stock_descontado)
            form.instance.precio_unitario = 0
            form.instance.precio_total = 0
        else:
            form.instance.stock_final = (form.instance.stock_inicial)+(form.instance.stock_descontado)
        
        
        productoStock_to_update = ProductoStock.objects.get(uuid= self.kwargs['pk'])
        
        

        productoStock_to_update.stock_disponible = form.instance.stock_final
        productoStock_to_update.save()
        return super(stocklogCreate, self).form_valid(form)
    

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)


        print("GET CONTEXT REGISTRO")
        print(str(self.kwargs['pk']))

        context['producto'] = ProductoStock.objects.get(uuid= self.kwargs['pk'])
        context['accion'] = self.kwargs['accion']
        print("CONTEXT")
        print(context)

        # Add in a QuerySet of all the books
        #context['categorias_list'] = CategoriaMenu.objects.all()
        return context
    

        
@method_decorator(login_required, name='dispatch')
class stocklogUpdate(generic.UpdateView):
    model = Stock
    form_class = StocklogForm
    success_url = reverse_lazy('stock:list')

    #template_name_suffix = '_update_form' 

   # def get_success_url(self):
       # return reverse_lazy('stockLog:list', args=[self.object.uuid]) + '?ok'

@method_decorator(login_required, name='dispatch')
class stocklogDelete(generic.DeleteView):
    model = Stock
    success_url = reverse_lazy('stock:logList')

