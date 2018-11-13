from django.urls import path
from .import views

urlpatterns = [
    path('', views.index , name="index"),
    path('crear/', views.crear , name="crear"),
    path('agregar_stock/', views.agregar_stock , name="agregar_stock"),
    path('eliminar/<id>', views.eliminar , name="eliminar"),
    path('editar/<id>/', views.editar , name="editar"),
    path('modificar/<id>/', views.modificar, name='modificar' ),
]