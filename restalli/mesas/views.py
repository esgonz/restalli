from django.shortcuts import render
from django.views import generic

from django.urls import reverse, reverse_lazy
from .models import Mesas
from .forms import MesasForm
class MesaList(generic.ListView):
	model = Mesas
	context_object_name = 'mesas_list'
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