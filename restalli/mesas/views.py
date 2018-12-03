from django.shortcuts import render
from django.views import generic

from django.urls import reverse, reverse_lazy
from .models import Mesas, Reserva
from .forms import MesasForm, ReservasForm
from pedidos.models import Pedido
class MesaList(generic.ListView):
	model = Mesas
	context_object_name = 'mesas_list'
	paginate_by = 100

class MesaListMovil(MesaList):
	model = Mesas
	context_object_name = 'mesas_list'
	template_name = "mesas/mesas_list_movil.html"
	paginate_by = 100


class MesaCreation(generic.edit.CreateView):
	model = Mesas
	form_class = MesasForm
	success_url = reverse_lazy('mesas:list')


class MesaUpdate(generic.UpdateView):
    model = Mesas
    form_class = MesasForm
    success_url = reverse_lazy('mesas:list')

class MesaDetailView(generic.DetailView):
    model = Mesas

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['reservas'] = Reserva.objects.filter(mesa_uuid= self.kwargs['pk'])
    	context['pedidos'] = Pedido.objects.filter(mesa= self.kwargs['pk'])
    	
    	print("PEDIDO")
    	context['pedidos']
    	print("Reservas")
    	context['reservas']
    	return context




class ReservaList(generic.ListView):
	model = Reserva
	context_object_name = 'reserva_list'
	paginate_by = 100

class ReservaCreation(generic.edit.CreateView):
	model = Reserva
	form_class = ReservasForm
	success_url = reverse_lazy('mesas:resList')
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		# Add in a QuerySet of all the books
		context['mesa'] = Mesas.objects.get(pk= self.request.GET['mesa'])

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

