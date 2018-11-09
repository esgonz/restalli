from django.urls import path
from . import views

urlpatterns = [
	path('', views.PageListView, name='pages'),
    #ex /menu/010101
    path('<int:pk>/<slug:slug>/', views.PageDetailView, name='page'),
    path('create/', views.PageCreate, name='create'),
    #menu /crear/seleccionarStock
    path('update/<int:pk>/', views.PageUpdate, name='update'),
    #ex /menu/create
    path('delete/<int:pk>/', views.PageDelete, name='delete')
]