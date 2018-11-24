from django.shortcuts import render
from django.views import generic
from .models import Empleados

class MesaList(generic.ListView):
	model = Empleados