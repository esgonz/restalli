from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required= True, help_text="Requerido, 254 caracteres como maximo")

    class Meta:
        model = User
        fields = {
            "username", "email", "password1", "password2"
        }
        ordering = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe, prueba con otro")
        return email