
from django.shortcuts import render

def principal(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def categoria(request):
	return render(request, 'categoria.html')