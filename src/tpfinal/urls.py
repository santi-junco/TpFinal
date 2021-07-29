"""tpfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tpfinal import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.blog.urls')),
    # path('posts', include('apps.blog.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about, name ='about'),    
    path('usuario', include('django.contrib.auth.urls')),
    path('', include('apps.usuario.urls')),
    #path('categoria/', views.categoria, name='categorias'),

    path('login/',auth.LoginView.as_view(template_name="usuario/login.html"), name='login'),
    path('logout/',auth.LogoutView.as_view(), name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

#Pesonalizacion de los titulos del administrador
admin.site.site_header = 'Administración del Blog Django'
admin.site.index_title = 'Blog Django'
admin.site.site_title = 'Administración del Blog'

