from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Mesas, Reserva
from .forms import MesasForm, ReservasForm
from pedidos.models import Pedido

@method_decorator(login_required, name='dispatch')
class MesaList(generic.ListView):
	model = Mesas
	context_object_name = 'mesas_list'
	paginate_by = 100

@method_decorator(login_required, name='dispatch')
class MesaListMovil(MesaList):
	model = Mesas
	context_object_name = 'mesas_list'
	template_name = "mesas/mesas_list_movil.html"
	paginate_by = 100

@method_decorator(login_required, name='dispatch')
class MesaCreation(generic.edit.CreateView):
    model = Mesas
    form_class = MesasForm
    template_name = "mesas/mesas_form.html"
    success_url = reverse_lazy('mesas:list')

@method_decorator(login_required, name='dispatch')
class MesaUpdate(generic.UpdateView):
    model = Mesas
    form_class = MesasForm
    template_name = "mesas/mesas_update_form.html"
    success_url = reverse_lazy('mesas:list')


@method_decorator(login_required, name='dispatch')
class MesaUpdateMovil(MesaUpdate):
    model = Mesas
    form_class = MesasForm
    template_name = "mesas/mesas_form_movil.html"
    success_url = reverse_lazy('mesas:mlist')



@method_decorator(login_required, name='dispatch')
class MesaDetailView(generic.DetailView):
    model = Mesas

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['reservas'] = Reserva.objects.filter()
    	pedidos_list = Pedido.objects.filter(mesa= self.kwargs['pk'])
    	
    	mesa_disponible = False

    	pedidos_acv_list = [] 
    	for pedido in pedidos_list:
    		print("pedido")
    		print(pedido.numero)

    		if pedido.estadoPedido =='INIT' or pedido.estadoPedido =='WAIT' or pedido.estadoPedido =='OK':
    			print("ACTIVO")
    			mesa_disponible = False
    			pedidos_acv_list.append(pedido)
    		else:
    			mesa_disponible = True
    			print(pedido.estadoPedido)
    		

    	if mesa_disponible:
    		print("MESA disponible")
    		self.object.estado = "FRE"
    		self.object.save()

    	context['pedidos'] = pedidos_acv_list
    	print("PEDIDOS")
    	context['pedidos'] 
    	print("Reservas")
    	context['reservas']
    	return context


@method_decorator(login_required, name='dispatch')
class MesaDetailViewMovil(MesaDetailView):
	template_name = "mesas/mesas_detail_movil.html"
	success_url = reverse_lazy('mesas:mlist')


class MesaDelete(generic.DeleteView):
	model = Mesas
	success_url = reverse_lazy('mesas:list')

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.soft_delete()
		return HttpResponseRedirect(self.get_success_url())	

class ReservaList(generic.ListView):
	model = Reserva
	context_object_name = 'reserva_list'
	paginate_by = 100

class ReservaCreation(generic.edit.CreateView):
    model = Reserva
    form_class = ReservasForm
    success_url = reverse_lazy('mesas:resList')
    template_name = "mesas/reserva_form.html"	
    

    def get_initial(self):
        print("GET INITIAL:")

        mes = Mesas.objects.get(pk= self.request.GET['mesa'])
        return {
            'mesa_uuid': mes.uuid
        }
        
    def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

		# Add in a QuerySet of all the books
        context['mesa'] = Mesas.objects.get(pk= self.request.GET['mesa'])


        context['reservas']=Reserva.objects.filter(mesa_uuid = self.request.GET['mesa'])
        print("RESERVAS")
        print(context['reservas'])
        #try to get cart, if cart doesnt exist, empty list
		#cart = self.request.session.get('cart', [])
		# Do stuff with cart
		#self.request.session['cart'] = cart
		#context['cart_list'] = self.request.session['cart']

		#try to get cart, if cart doesnt exist, empty list
		#total_cart = self.request.session.get('total_cart', [])
	
		# Do stuff with cart
		#self.request.session['total_cart'] = total_cart
		#context['total_cart'] = self.request.session['total_cart']


		#print("LIST CART:")
		#print(context['cart_list'])
        return context

class ReservaUpdate(generic.UpdateView):
    model = Reserva
    form_class = ReservasForm
    template_name = "mesas/reserva_update_form.html"
    success_url = reverse_lazy('mesas:resList')

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['mesa'] = Mesas.objects.get(pk= self.object.mesa_uuid.uuid)


        context['reservas']=Reserva.objects.filter(mesa_uuid = self.object.mesa_uuid.uuid)

        return context

class ReservaDelete(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy('mesas:resList')


class ReservaDetailView(generic.DetailView):
    model = Mesas
    form_class = ReservasForm
    success_url = reverse_lazy('mesas:resList')
    
    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['mesa'] = Mesas.objects.get(pk= self.request.GET['mesa'])
    	context['pedido'] = Pedido.objects.filter(mesa= self.request.GET['mesa'])
    	print("PEDIDO")
    	context['pedido']
    	return context

