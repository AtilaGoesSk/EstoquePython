from django.shortcuts import render,redirect, get_object_or_404
from .models import Fornecedor, Produto

# Create your views here.
def home(request):
    return render(request, 'home.html')

#-----------------------------------------------------------------------
# Produtos

def produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': lista_produtos})

#------------------------

def novo_produto(request):
    fornecedores = Fornecedor.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        fornecedor_id = request.POST.get('fornecedor')

        fornecedor = None
        if fornecedor_id:
            fornecedor = Fornecedor.objects.get(id=fornecedor_id)

        Produto.objects.create(
            nome=nome,
            descricao=descricao,  
            preco=preco,
            quantidade=quantidade,
            fornecedor=fornecedor
        )

        return redirect('produtos')

    return render(request, 'novo_produto.html', {
        'fornecedores': fornecedores
    })

#------------------------

def editar_produto(request, id):

    produto = get_object_or_404(Produto, id=id)
    fornecedores = Fornecedor.objects.all()

    if request.method == "POST":
        produto.nome = request.POST.get("nome")
        produto.descricao = request.POST.get("descricao")
        produto.preco = request.POST.get("preco")
        produto.quantidade = request.POST.get("quantidade")

        fornecedor_id = request.POST.get("fornecedor")

        if fornecedor_id:
            produto.fornecedor = Fornecedor.objects.get(id=fornecedor_id)
        else:
            produto.fornecedor = None

        produto.save()

        return redirect('produtos')

    return render(request, 'novo_produto.html', {
        'produto': produto,
        'fornecedores': fornecedores
    })
#------------------------

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()

    return redirect('produtos')

#-----------------------------------------------------------------------
# Fornecedores

def fornecedores(request):
    lista_fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores.html', {'fornecedores': lista_fornecedores})

def novo_fornecedor(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        Fornecedor.objects.create(
            nome=nome,
            email=email,
            telefone=telefone
        )

        return redirect('fornecedores')

    return render(request, 'novo_fornecedor.html')

def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)

    if request.method == "POST":
        fornecedor.nome = request.POST.get("nome")
        fornecedor.email = request.POST.get("email")
        fornecedor.telefone = request.POST.get("telefone")

        fornecedor.save()
        return redirect('fornecedores')

    return render(request, 'novo_fornecedor.html', {'fornecedor': fornecedor})

def deletar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    fornecedor.delete()

    return redirect('fornecedores')