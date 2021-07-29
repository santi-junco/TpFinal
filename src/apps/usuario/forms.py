from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from ..usuario.models import Usuario
# from .forms import Formulario_Post


class Formulario_Registro_Usuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']