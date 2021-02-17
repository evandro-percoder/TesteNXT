from django.shortcuts import render
from django.http import HttpResponse

#adicionei agora
from . import urls
from .models import Cliente, Endereco


def home(request):
    return render(request, "base.html", {})

def produtos(request):
    return render(request, "produtos.html", {})

def cadastro(*args, **kwargs):
    return HttpResponse()