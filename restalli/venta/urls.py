from django.urls import path
from . import views
app_name = 'venta'
urlpatterns = [
    path('', views.ventaListView.as_view(), name='list'),
    path('venta/nuevo/', views.ventaCreate.as_view(), name='create'),
    path('venta/<pk>/', views.ventaDetailView.as_view(), name='detail'),    
    path('venta/editar/<pk>/', views.ventaUpdate.as_view(), name='update'),
    path('venta/eliminar/<pk>/', views.ventaDelete.as_view(), name='delete'),
]
