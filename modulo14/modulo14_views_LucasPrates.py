from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def listar_produtos(request):
    termo = request.GET.get('busca', '')
    produtos = Produto.objects.filter(nome__icontains=termo)
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        Produto.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
            preco=request.POST.get('preco'),
            quantidade=request.POST.get('quantidade')
        )
        return redirect('listar_produtos')
    return render(request, 'produtos/cadastrar.html')

def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/atualizar.html', {'produto': produto})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')