from django.shortcuts import redirect, render, get_object_or_404
from SegundaAtividade.models import Endereco
from SegundaAtividade.forms import EnderecoForm

def home(request):
    enderecos = Endereco.objects.all()       
    
    return render(request, 'Endereco/home.html', {
        "listaEnderecos" : enderecos,
    })
    
def insert(request):
    form = EnderecoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('endereco.home')
    
    return render(request, 'Endereco/insert.html', {
        "form" : form,
    })
    
def edit(request, id):
    enderecoSelect = get_object_or_404(Endereco, pk=id)
    form = EnderecoForm(request.POST or None, instance=enderecoSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('endereco.home')
    
    return render(request, 'Endereco/edit.html', {
        'form' : form,
        'nome' : enderecoSelect.rua
    })
    
def delete(request, id):
    enderecoSelect = get_object_or_404(Endereco, pk=id)
    enderecoSelect.delete()
    
    return redirect('endereco.home')
