from django.shortcuts import redirect, render, get_object_or_404
from meuapp.models import Funcionario
from meuapp.forms import FuncionarioForm

def home(request):
    funcionarios = Funcionario.objects.all()       
    
    return render(request, 'Funcionario/home.html', {
        "listaFuncionarios" : funcionarios,
    })
    
def insert(request):
    form = FuncionarioForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('funcionario.home')
    
    return render(request, 'Funcionario/insert.html', {
        "form" : form,
    })
    
def edit(request, id, nome):
    funcionarioSelect = get_object_or_404(Funcionario, pk=id)
    form = FuncionarioForm(request.POST or None, instance=funcionarioSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('funcionario.home')
    
    return render(request, 'Funcionario/edit.html', {
        'form' : form,
        'nome' : nome
    })
    
def delete(request, id):
    funcionarioSelect = get_object_or_404(Funcionario, pk=id)
    funcionarioSelect.delete()
    
    return redirect('funcionario.home')
