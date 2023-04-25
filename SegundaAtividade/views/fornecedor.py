from django.shortcuts import redirect, render, get_object_or_404
from SegundaAtividade.models import Fornecedor
from SegundaAtividade.forms import FornecedorForm

def home(request):
    Fornecedores = Fornecedor.objects.all()       
    
    return render(request, 'Fornecedor/home.html', {
        "listaFornecedores" : Fornecedores,
    })
    
def insert(request):
    form = FornecedorForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('fornecedor.home')
    
    return render(request, 'Fornecedor/insert.html', {
        "form" : form,
    })
    
def edit(request, id, nome):
    fornecedorSelect = get_object_or_404(Fornecedor, pk=id)
    form = FornecedorForm(request.POST or None, instance=fornecedorSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('fornecedor.home')
    
    return render(request, 'Fornecedor/edit.html', {
        'form' : form,
        'nome' : nome
    })
    
def delete(request, id):
    fornecedorSelect = get_object_or_404(Fornecedor, pk=id)
    fornecedorSelect.delete()
    
    return redirect(home)