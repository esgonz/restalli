from django.urls import path
from .views import SignUpView, PerfilesUpdate, userListView

app_name = 'registration'
urlpatterns = [
path('signup/', SignUpView.as_view(), name="signup"),
path('perfiles/', PerfilesUpdate.as_view(), name="perfiles"),
path('', userListView.as_view(), name="list"),
path('editar/<pk>/', PerfilesUpdate.as_view(), name="update")

]