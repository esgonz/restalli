from django.shortcuts import render
from django.views import generic
from .models import Mesas

class MesaList(generic.ListView):
	model = Mesas