from .forms import UserCreationForm, UserChangeForm
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import User


class SignUpView(CreateView):
    form_class= UserCreationForm
    template_name = 'registration/signup.html'
    model = User
    
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    """def get_forms(self, form_class= None):
        form = super(SignUpView, self).get_form()
        #modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre Usuario'}),
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-','placeholder':'Email'}),
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-1','placeholder':'Contraseña'}),
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-','placeholder':'Reingrese contraseña'}),
        return form"""
#@method_decorator(login_required, name='dispatch')
#class PerfilesUpdate(TemplateView):
 #   template_name = 'registration/perfiles_form.html'

@method_decorator(login_required, name='dispatch')
class PerfilesUpdate(UpdateView):
    form_class= UserChangeForm
    model = User
    sucess_url = reverse_lazy('registration:list')
    template_name = 'registration/perfiles_form.html'

    def get_success_url(self):
        return self.sucess_url

@method_decorator(login_required, name='dispatch')
class userListView(ListView):
    model = User
    context_object_name = 'usuarios_list'
   
