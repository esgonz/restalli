from django.urls import path
from . import views
app_name = 'venta'
urlpatterns = [
    path('', views.ventaListView.as_view(), name='list'),
    path('/nuevo/', views.ventaCreate.as_view(), name='create'),
    path('/<pk>/', views.ventaDetailView.as_view(), name='detail'),    
    path('/editar/<pk>/', views.ventaUpdate.as_view(), name='update'),
    path('/eliminar/<pk>/', views.ventaDelete.as_view(), name='delete'),
]
