from django.shortcuts import render
from django.views import generic
from .models import Empleados

class EmpleadoList(generic.ListView):
	model = Empleados