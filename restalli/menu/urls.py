from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
	path('', views.index, name='index'),
    #ex /menu/010101
    path('<int:producto_uuid>/', views.editar, name='editar'),
    #menu /crear/seleccionarStock
    path('nuevo/', views.seleccionarStock, name='seleccionarStock'),
    #ex /menu/create
    path('nuevo/paso2/', views.crear, name='crear'),
    #ex /menu/listar
    path('lista/', views.listar, name='listar')
]