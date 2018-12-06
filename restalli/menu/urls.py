from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.MenuList.as_view(), name='list'),
    path('nuevo/', views.MenuCreation.as_view(), name='create'),
    path('ver/<pk>/', views.MenuDetail.as_view(), name='detail'),    
    path('editar/<pk>/', views.MenuUpdate.as_view(), name='update'),
    path('eliminar/<pk>/', views.MenuDelete.as_view(), name='delete'),
    path('categoria/', views.CategoriaList.as_view(), name='catList'),
    path('categoria/nuevo/', views.CategoriaCreation.as_view(), name='catCreate'),
    path('categoria/<pk>/', views.CategoriaDetail.as_view(), name='catDetail'),    
    path('categoria/editar/<pk>/', views.CategoriaUpdate.as_view(), name='catUpdate'),
    path('categoria/eliminar/<pk>/', views.CategoriaDelete.as_view(), name='catDelete'),
    path('nuevo/producto-menu/seleccion/<producto>', views.ProductosMenuStockList.as_view(), name='stockSelection'),
    path('nuevo/producto-menu/crear/', views.ProductosMenuStockCreation.as_view(), name='stockCreate'),
    path('nuevo/producto-menu/<pk>/', views.ProductosMenuStockDetail.as_view(), name='stockDetail'),    
    path('nuevo/producto-menu/editar/<pk>/', views.ProductosMenuStockUpdate.as_view(), name='stockUpdate'),
    path('nuevo/producto-menu/eliminar/<pk>/', views.ProductosMenuStockDelete.as_view(), name='stockDelete'),

]