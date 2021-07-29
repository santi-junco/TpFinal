  
from django.urls import path
from . import views
from . views import *

# Un home esta de mas, nuevo y crear hacen lo mismo, dejo crear porque se usa la clase
urlpatterns = [
  path('', Home.as_view(), name = 'home'),
  #path('home/', Home.as_view(), name = 'home'),
  path('posts/<int:pk>', views.post , name = 'posts'),
  path('crear/', views.Alta_post.as_view(), name = 'alta_post'),
  #path('nuevo/', post_nuevo, name = 'nuevo'),
  path('editar/<int:pk>/',views.Editar_post.as_view(), name= 'editar'),
  path('comentario/<int:pk>/<int:post_id>/',views.Editar_comentario.as_view(), name='edicion'),
  path('eliminar/<int:pk>/',eliminar_post, name= 'eliminar'),
  path('eliminarcoment/<int:coment_id>/<int:post_id>/', eliminar_comentario, name='eliminar_comentario'),
  #path('crear_usuario/', views.Alta_usuario.as_view(), name='crear_usuario')
  path('categoria/<str:categ>', views.vista_categorias, name = 'categorias'),
  # path('filtrar/',views.filtroF),
  path('filtrovista/', views.filt),
  path('filtro/',views.filt, name='filtro'),
  path('categoria/<str:categ>/filtro/', views.filt_categorias),
  path('usuarios/<str:usuario>/', views.filtrar_usuario, name = 'usuarios'),
 
]