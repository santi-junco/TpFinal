
from django.urls import path
#from ..usuario.views import *

from ..usuario import views
from . views import *
from django.contrib.auth import views as auth

# Un home esta de mas, nuevo y crear hacen lo mismo, dejo crear porque se usa la clase
urlpatterns = [

  
  path('registrar/', views.Alta_usuario.as_view(), name='crear_usuario'),
  path('login/',auth.LoginView.as_view(template_name="usuario/login.html"), name='login'),
   path('logout/',auth.LogoutView.as_view(), name="logout"),
  
]