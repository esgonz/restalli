from django.urls import path
from . import views

app_name = 'pedidos'
urlpatterns = [
	path('', views.PedidoList.as_view(), name='list'),
    path('menu/', views.MenuOfertList.as_view(), name='menu'),
    path('nuevo/', views.PedidoCreation.as_view(), name='create'),
    path('ver/<pk>/', views.PedidoDetail.as_view(), name='detail'),    
    path('editar/<pk>/', views.PedidoUpdate.as_view(), name='update'),
]