
from django.shortcuts import render
from django.http import HttpResponse
from .models import Filme
# Create your views here.



def filme(request,id):
    
    return render(
        request = request,
        template_name= "filmes/filme.html",
        context= {"filmes":Filme.objects.get(id=id)}
    )


def index(request):
    
    return render(
        request = request,
        template_name= "filmes/index.html",
        context= {"filmes":Filme.objects.all()}
    )