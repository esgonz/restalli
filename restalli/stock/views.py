from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.template import loader
from .models import ProductoStock, Stock
from .forms import StockForm, StocklogForm

# index 
class IndexView(generic.ListView):
    context_object_name = 'latest_stock_list'

#class StaffRequiredMixin(object):
 # def dispatch(self, request, *args, **kwargs):
  #      if not request.user.is_staff:
   #         return redirect(reverse_lazy('admin:login'))
    #    return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)   

# Create your views here.aa
class stockListView(generic.ListView):
    model = ProductoStock
    paginate_by = 3
    context_object_name = 'productoStock_list'


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
                return ProductoStock.objects.filter(categoria=filter_val)
            else:
                #si no, devuelvo todos los productos
                return ProductoStock.objects.all()
        


class stockDetailView(generic.DetailView):
    model = ProductoStock
#success_url = reverse_lazy('stock:list')

class stockCreate(generic.CreateView):
    model = ProductoStock
    form_class = StockForm
    #success_url = reverse_lazy('stock:create')

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

    def get_initial(self):
        print("GET INITIAL:")

        producto = ProductoStock.objects.get(uuid= self.kwargs['pk'])

        return {
            'producto_uuid': self.kwargs['pk'],
            'stock_inicial': producto.stock_disponible,
        }

    def get(self, request, *args, **kwargs):

        
        #self.object = self.get_object(queryset=Publisher.objects.all())
        self.producto_uuid = kwargs.get("pk")
        return super().get(request, *args, **kwargs)

    """def post(self, request, *args, **kwargs):
        print("POST:")
        
        #self.object = self.get_object(queryset=Publisher.objects.all())
        self.producto_uuid = kwargs.get("pk")
        return super().get(request, *args, **kwargs)"""
    
    def form_valid(self, form):
        accion =self.kwargs['accion']
        if accion == 'descontar':
            form.instance.stock_final = (form.instance.stock_inicial)-(form.instance.stock_descontado)
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
        print(str(self.producto_uuid))

        context['producto'] = ProductoStock.objects.get(uuid= self.producto_uuid)
        print("CONTEXT")
        print(context)

        # Add in a QuerySet of all the books
        #context['categorias_list'] = CategoriaMenu.objects.all()
        return context
    

        

class stocklogUpdate(generic.UpdateView):
    model = Stock
    form_class = StocklogForm
    success_url = reverse_lazy('stock:list')

    #template_name_suffix = '_update_form' 

   # def get_success_url(self):
       # return reverse_lazy('stockLog:list', args=[self.object.uuid]) + '?ok'

class stocklogDelete(generic.DeleteView):
    model = Stock
    success_url = reverse_lazy('stock:logList')




