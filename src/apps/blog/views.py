from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from .models import *
from .forms import Formulario_Alta_Post, Formulario_Alta_Comentario, Filtro_Fecha
from django.http import HttpResponse, HttpResponseRedirect
from ..usuario.models import Usuario
from datetime import datetime
from django.core.paginator import Paginator

#Creacion de las vistas

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#Creacion de las vistas

class Home(ListView):
	model = Post
	template_name = 'blog/home.html'
	ordering = ['-id']
	paginate_by = 4

	def  get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		categoria = Categoria.objects.all()
		context['categoria'] = categoria
		context['fecha']=Filtro_Fecha
		return context

#def vista_categorias(request, categ):
#	existe = Categoria.objects.filter(categoria_nombre=categ)
#	#page = request.GET.get('page', 1)
#	categoria_posts = Post.objects.filter(categoria=categ)


#	paginator = Paginator(categoria_posts, 1)
#	page_number = request.GET.get('page')
#	page_obj = paginator.get_page(page_number)
	#return render(request, 'list.html', {'page_obj': page_obj})
#	return render(request, 'blog/categorias.html', {'page_obj': page_obj}, {'existe':existe})
	
#class Filtro_fecha(ListView):
#	model = Post
#	template_name = 'blog/home.html'
#
#	def get_context_data(self,**kwargs):
#		context= super().get_context_data(**kwargs)
#		context['fecha']=Filtro_Fecha
#		return context
#
#	def get_queryset(self,**kwargs):
#		fecha=self.kwargs['filtro_fecha']
#		return Post.objects.filter(fecha_publicacion=fecha)
#utilice una funcion para definir esta vista porque se necesita utilizar los dos modelos
# def filtroF(request):
# 	return render(request,"blog/filtro.html")

def filt(request):
	desde=request.GET['desde']
	desde = datetime.strptime(desde, '%Y-%m-%d')
	hasta=request.GET['hasta']
	hasta = datetime.strptime(hasta, '%Y-%m-%d')
	page_obj=Post.objects.filter(fecha_publicacion__gte=desde, fecha_publicacion__lte=hasta).order_by('-id')
	categoria = Categoria.objects.all()

	#paginator = Paginator(posts, 4)
	#page_number = request.GET.get('page')
	#page_obj = paginator.get_page(page_number)


	return render(request, 'blog/filtro.html', {'page_obj':page_obj, 'desde':request.GET['desde'], 'hasta':request.GET['hasta'], 'categoria':categoria})



def filt_categorias(request, categ):
	existe = Categoria.objects.filter(categoria_nombre=categ)
	desde=request.GET['desde']
	desde = datetime.strptime(desde, '%Y-%m-%d')
	hasta=request.GET['hasta']
	hasta = datetime.strptime(hasta, '%Y-%m-%d')
	page_obj=Post.objects.filter(fecha_publicacion__gte=desde, fecha_publicacion__lte=hasta, categoria=categ).order_by('-id')
	#return HttpResponse(posts)

	categoria = Categoria.objects.all()

	#return render(request, 'list.html', {'page_obj': page_obj})


	return render(request, 'blog/filtro.html', {'page_obj':page_obj, 'desde':request.GET['desde'], 'hasta':request.GET['hasta'], 'es_categ':existe, 'categoria':categoria, 'categ':categ.title()})


def post(request, pk):
	post = Post.objects.get(id=pk)
	comentarios = Comentario.objects.filter(post= post.id)
	
	###ESTA PARTE ES DEL FORMULARIO PARA EL COMENTARIO####
	if request.method == 'POST':
		form = Formulario_Alta_Comentario(request.POST)
		if form.is_valid():
			comentario = form.save(commit=False)
			comentario.post = post
			comentario.save()


			#return redirect('home') ### Te devuelve a la home despues de comentar, me parece que no sirve 
			#por eso lo anulo
	else:
		form = Formulario_Alta_Comentario()
	###########  ACA TERMINA LO DEL FORMULARIO PARA EL COMENTARIO     ##########	
	ctx = {'post':post, 'comentarios': comentarios, 'form' : form}
	return render(request, 'blog/post.html', ctx)

class Editar_post(LoginRequiredMixin ,UpdateView):
	model = Post
	form_class = Formulario_Alta_Post
	template_name='blog/altaPost.html'
	success_url=reverse_lazy('home')

class Editar_comentario(LoginRequiredMixin,UpdateView):
	model = Comentario
	form_class = Formulario_Alta_Comentario
	template_name='blog/comentario.html'	
	# success_url='/posts/5'

	def get_success_url(self):
		# Assuming there is a ForeignKey from Comment to Post in your model
		post = self.object.post_id
		return reverse_lazy( 'posts', kwargs={'pk': post})


# class Eliminar_post(DeleteView):
# 	model=Post
# 	form_class = Formulario_Alta_Post
# 	template_name='blog/bajaPost.html'
# 	success_url=reverse_lazy('home')


def eliminar_post(request, pk):
	post = Post.objects.get(id=pk)
	post.delete()
	return HttpResponseRedirect('/')

def eliminar_comentario(request, coment_id, post_id):
	comentario = Comentario.objects.get(id=coment_id)
	comentario.delete()
	return HttpResponseRedirect("/posts/{}".format(post_id))
	

# class eliminar_comentario(DeleteView):
# 	model = Comentario
# 	form_class = Formulario_Alta_Comentario
# 	template_name='blog/post.html'
# 	success_url=reverse_lazy('home')
	
class Alta_post(LoginRequiredMixin ,CreateView):
	model = Post 
	form_class = Formulario_Alta_Post
	template_name = 'blog/altaPost.html'
	success_url = reverse_lazy('home')


def vista_categorias(request, categ):
	page_obj = Post.objects.filter(categoria=categ).order_by('-id')
	existe = Categoria.objects.filter(categoria_nombre=categ)
	categoria = Categoria.objects.all()
	es_categ = True
	#return render(request, 'list.html', {'page_obj': page_obj})

	return render(request, 'blog/categorias.html', {'page_obj':page_obj, 'es_categ':es_categ, 'categ':categ.title(), 'existe':existe,'categoria':categoria})

def filtrar_usuario(request,usuario):
	nombre = 'Error!'
	page_obj = None

	existe = Usuario.objects.filter(username=usuario)

	if(existe):
		user = Usuario.objects.get(username=usuario)
		page_obj = Post.objects.filter(id_user=user.id)
		nombre = user.username.upper()

	categoria = Categoria.objects.all()
	return render(request,'blog/usuarios.html', {'page_obj':page_obj,'categoria':categoria, 'existe':existe, 'nombre':nombre})


#class Alta_comentario(CreateView):
	#model = Comentario 
	#form_class = Formulario_Alta_Comentario
	#template_name = 'blog/post.html'
	#success_url = reverse_lazy('home')

# No hace falta, se esta usando la clase "Alta_post"
#def post_nuevo(request):
#	if request.method == 'POST':
#		form = Formulario_Alta_Post(request.POST)
#		if form.is_valid():
#			form.save()
#			return redirect('home')
#	else:
#		
#		form = Formulario_Alta_Post()
#
#	ctx = {'form' : form}
#	return render(request, 'blog/altaPost.html', ctx)

	# else:
	# 	form = Formulario_Alta_Post(request.POST)
	# 	ctx= {'form' : form}
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('home')

#class Alta_usuario(CreateView):
#    model = Usuario
 #   form_class = Formulario_Registro_Usuario
  #  template_name = 'usuario/altaUsuario.html'
   # #success_url = reverse_lazy('home')