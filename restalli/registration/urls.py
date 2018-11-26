from django.urls import path
from .views import SignUpView, PerfilesUpdate

app_name = 'registration'
urlpatterns = [
path('signup/', SignUpView.as_view(), name="signup"),
path('perfiles/', PerfilesUpdate.as_view(), name="perfiles"),

]