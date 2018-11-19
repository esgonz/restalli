from django.urls import path
from . import views

app_name = 'pedidos'
urlpatterns = [
    path('', views.MenuOfertList.as_view(), name='list'),
    path('nuevo/', views.PedidoCreation.as_view(), name='create'),
    path('ver/<pk>/', views.PedidoDetail.as_view(), name='detail'),    
    path('editar/<pk>/', views.PedidoUpdate.as_view(), name='update'),
]