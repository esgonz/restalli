from django.urls import path

from .views import HomePageView, HomePageViewMovil
app_name = 'comun'
urlpatterns = [
    path('', HomePageView.as_view(), name='dashboard'),
    path('movil/', HomePageViewMovil.as_view(), name='mdashboard'),
]