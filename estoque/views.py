from django.shortcuts import render,redirect, get_object_or_404
from .models import Produtos

# Create your views here.
def home(request):
    return render(request, 'home.html')

def produtos(request):
    lista_produtos = Produtos.objects.all()
    return render(request, 'produtos.html', {'produtos': lista_produtos})

def novo_produto(request):
    return render(request, 'novo_produto.html')

def editar_produto(request, id):
    return render(request, 'editar_produto.html')

def deletar_produto(request, id):
    return redirect('produtos')