from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template import loader
from .models import Venta
from .forms import VentaForm
# Create your views here.

#venta Logica

class ventaListView(generic.ListView):
    model = Venta

class ventaDetailView(generic.DetailView):
    model = Venta

class ventaCreate(generic.CreateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('venta:list')

class ventaUpdate(generic.UpdateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('venta:list')

    #template_name_suffix = '_update_form' 

   # def get_success_url(self):
       # return reverse_lazy('stockLog:list', args=[self.object.uuid]) + '?ok'

class ventaDelete(generic.DeleteView):
    model = Venta
    success_url = reverse_lazy('venta:list')
