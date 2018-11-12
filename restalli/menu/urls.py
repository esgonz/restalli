from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
    #ex /menu/010101
    path('<int:pk>/', views.EditarView.as_view(), name='editar'),
    #menu /crear/seleccionarStock
    #path('nuevo/', views.seleccionarStockView.as_view(), name='seleccionarStock'),
    #ex /menu/create
    path('nuevo/paso2/', views.CrearView.as_view(), name='crear'),
    #ex /menu/listar
    #path('lista/', views.listarView.as_view(), name='listar')
]