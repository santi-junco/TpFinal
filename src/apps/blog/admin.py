from django.contrib import admin
from .models import Post, Comentario, Categoria


# Register your models here.

class BusquedaAdmin(admin.ModelAdmin):
    search_fields =['categoria','fecha_publicacion']
    list_filter=('categoria',)

#Registrar en la administracion 

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Categoria)