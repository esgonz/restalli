from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
	path('', views.stockListView.as_view(), name='list'),
    path('nuevo/', views.stockCreate.as_view(), name='create'),
    path('detalle/<pk>/', views.stockDetailView.as_view(), name='detail'),
    path('actualizar/<pk>/', views.stockUpdate.as_view(), name='update'),
    path('eliminar/<pk>/', views.stockDelete.as_view(), name='delete'),
    path('registro/', views.stocklogListView.as_view(), name='logList'),
    path('registro/nuevo/<pk>/<accion>/', views.stocklogCreate.as_view(), name='logCreate'),
    path('registro/detalle/<pk>/', views.stocklogDetailView.as_view(), name='logDetail'),    
    path('registro/editar/<pk>/', views.stocklogUpdate.as_view(), name='logUpdate'),
    path('registro/eliminar/<pk>/', views.stocklogDelete.as_view(), name='logDelete'),
]