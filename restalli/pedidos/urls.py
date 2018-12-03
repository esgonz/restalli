from django.urls import path
from . import views

app_name = 'pedidos'
urlpatterns = [
	path('', views.PedidoList.as_view(), name='list'),
	path('movil/', views.PedidoListMovil.as_view(), name='mlist'),
    path('menu/', views.MenuOfertList.as_view(), name='menu'),
    path('movil/menu/', views.MenuOfertaListMovil.as_view(), name='mmenu'),
    path('nuevo/', views.PedidoCreation.as_view(), name='create'),
    path('movil/nuevo/', views.PedidoCreationMovil.as_view(), name='mcreate'),
    path('ver/<pk>/', views.PedidoDetail.as_view(), name='detail'),    
    path('editar/<pk>/', views.PedidoUpdate.as_view(), name='update'),
]