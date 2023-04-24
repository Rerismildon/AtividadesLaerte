from django.shortcuts import redirect, render, get_object_or_404
from SegundaAtividade.models import Produto
from SegundaAtividade.forms import ProdutoForm

def home(request):
    Produtos = Produto.objects.all()       
    
    return render(request, 'Produto/home.html', {
        "listaProdutos" : Produtos,
    })
    
def insert(request):
    form = ProdutoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('produto.home')
    
    return render(request, 'Produto/insert.html', {
        "form" : form,
    })
    
def edit(request, id, nome):
    produtoSelect = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produtoSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('produto.home')
    
    return render(request, 'Produto/edit.html', {
        'form' : form,
        'nome' : nome
    })
    
def delete(request, id):
    produtoSelect = get_object_or_404(Produto, pk=id)
    produtoSelect.delete()
    
    return redirect(home)