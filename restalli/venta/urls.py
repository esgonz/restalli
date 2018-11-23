from django.urls import path
from . import views
app_name = 'venta'
urlpatterns = [
    path('', views.ventaListView.as_view(), name='list'),
    path('venta/nuevo/', views.ventaCreate.as_view(), name='Create'),
    path('venta/<pk>/', views.ventaDetailView.as_view(), name='Detail'),    
    path('venta/editar/<pk>/', views.ventaUpdate.as_view(), name='Update'),
    path('venta/eliminar/<pk>/', views.ventaDelete.as_view(), name='Delete'),
]
