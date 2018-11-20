from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
	path('', views.stockListView.as_view(), name='list'),
    #ex /stock/010101
    path('Create/', views.stockCreate.as_view(), name='Create'),
    path('<pk>/', views.stockDetailView.as_view(), name='detail'),
    #menu /crear/seleccionarStock
    path('update/<pk>/', views.stockUpdate.as_view(), name='update'),
    #ex /menu/create
    path('delete/<pk>/', views.stockDelete.as_view(), name='delete'),
    #eliminar
    path('stocklog/', views.stocklogListView.as_view(), name='listlog'),
    path('stocklog/nuevo/', views.stocklogCreate.as_view(), name='logCreate'),
    path('stocklog/<pk>/', views.stocklogDetailView.as_view(), name='logDetail'),    
    path('stocklog/editar/<pk>/', views.stocklogUpdate.as_view(), name='logUpdate'),
    path('stocklog/eliminar/<pk>/', views.stocklogDelete.as_view(), name='logDelete'),


    path('categoria/', views.CategoriaListView.as_view(), name='catList'),
    path('categoria/nuevo/', views.CategoriaCreate.as_view(), name='catCreate'),
    path('categoria/<pk>/', views.CategoriaDetailView.as_view(), name='catDetail'),    
    path('categoria/editar/<pk>/', views.CategoriaUpdate.as_view(), name='catUpdate'),
    path('categoria/eliminar/<pk>/', views.CategoriaDeleteView.as_view(), name='catDelete'),
]