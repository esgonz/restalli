from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Venta
from .forms import VentaForm
from pedidos.models import Pedido
# Create your views here.

#venta Logica

@method_decorator(login_required, name='dispatch')
class ventaListView(generic.ListView):
    model = Venta
    context_object_name = 'ventas_list'

@method_decorator(login_required, name='dispatch')
class ventaListViewMovil(ventaListView):
    template_name="venta/venta_list_movil.html"

@method_decorator(login_required, name='dispatch')
class ventaDetailView(generic.DetailView):
    model = Venta

@method_decorator(login_required, name='dispatch')
class ventaDetailViewMovil(ventaDetailView):
    template_name="venta/venta_detail_movil.html"


@method_decorator(login_required, name='dispatch')
class ventaCreate(generic.CreateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('venta:list')

    def get_initial(self):
        print("GET INITIAL:")

        
        pedido = Pedido.objects.get(uuid= self.request.GET['uuid'])

        return {
            'pedido_uuid': pedido.uuid,
            'monto': int(pedido.total),
            'monto_propina': int(float(pedido.total)*0.10),
        }



    def form_valid(self, form):
        print("FORM VALID")
        """accion =self.kwargs['accion']
        if accion == 'descontar':
            form.instance.stock_final = (form.instance.stock_inicial)-(form.instance.stock_descontado)
            form.instance.precio_unitario = 0
            form.instance.precio_total = 0
        else:
            form.instance.stock_final = (form.instance.stock_inicial)+(form.instance.stock_descontado)
        """
        print("uuid:")
        print(self.request.GET['uuid'])
        pedido_to_update = Pedido.objects.get(pk= self.request.GET['uuid'])
        print("PEDIDO:")
        print(pedido_to_update)

        pedido_to_update.estadoPedido = "PGD"
        pedido_to_update.save()

        form.instance.pedido_uuid = pedido_to_update
        return super(ventaCreate, self).form_valid(form)

    """def get(self, request, *args, **kwargs):

        
        #self.object = self.get_object(queryset=Publisher.objects.all())
        self.producto_uuid = kwargs.get("pk")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("POST:")
        
        #self.object = self.get_object(queryset=Publisher.objects.all())
        self.producto_uuid = kwargs.get("pk")
        return super(stocklogCreate, self).get(request, *args, **kwargs)
    
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
        return contextxw"""

@method_decorator(login_required, name='dispatch')
class ventaCreateMovil(ventaCreate):
    template_name="venta/venta_form_movil.html"
    success_url = reverse_lazy('pedidos:mlist')

@method_decorator(login_required, name='dispatch')
class ventaUpdate(generic.UpdateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('venta:list')

    #template_name_suffix = '_update_form' 

   # def get_success_url(self):
       # return reverse_lazy('stockLog:list', args=[self.object.uuid]) + '?ok'


@method_decorator(login_required, name='dispatch')
class ventaUpdateMovil(ventaUpdate):
    model = Venta
    form_class = VentaForm
    template_name="venta/venta_update_form_movil.html"
    success_url = reverse_lazy('venta:mlist')

    #template_name_suffix = '_update_form' 

   # def get_success_url(self):
       # return reverse_lazy('stockLog:list', args=[self.object.uuid]) + '?ok'

@method_decorator(login_required, name='dispatch')
class ventaDelete(generic.DeleteView):
    model = Venta
    success_url = reverse_lazy('venta:list')
