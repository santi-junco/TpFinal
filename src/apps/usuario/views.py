from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy, reverse
#from .models import Post, Comentario
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from ..usuario.models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

#Creacion de las vistas


class Alta_usuario(CreateView):
    model = Usuario
    form_class = Formulario_Registro_Usuario
    template_name = 'usuario/altaUsuario.html'
    success_url = reverse_lazy('home')