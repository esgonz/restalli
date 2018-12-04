from django.urls import path
from . import views
app_name = 'venta'
urlpatterns = [
    path('', views.ventaListView.as_view(), name='list'),
    path('movil/', views.ventaListViewMovil.as_view(), name='mlist'),
    path('nuevo/', views.ventaCreate.as_view(), name='create'),
    path('movil/nuevo/', views.ventaCreateMovil.as_view(), name='mcreate'),
    path('ver/<pk>/', views.ventaDetailView.as_view(), name='detail'),
    path('movil/ver/<pk>/', views.ventaDetailViewMovil.as_view(), name='mdetail'),    
    path('editar/<pk>/', views.ventaUpdate.as_view(), name='update'),
    path('eliminar/<pk>/', views.ventaDelete.as_view(), name='delete'),
]
