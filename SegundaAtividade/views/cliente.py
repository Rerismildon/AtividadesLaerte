from django.shortcuts import redirect, render, get_object_or_404
from SegundaAtividade.models import Cliente
from SegundaAtividade.forms import ClienteForm

def home(request):
    Clientes = Cliente.objects.all()       
    
    return render(request, 'Cliente/home.html', {
        "listaClientes" : Clientes,
    })
    
def insert(request):
    form = ClienteForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('cliente.home')
    
    return render(request, 'Cliente/insert.html', {
        "form" : form,
    })
    
def edit(request, id):
    clienteSelect = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=clienteSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('cliente.home')
    
    return render(request, 'Cliente/edit.html', {
        'form' : form,
        'nome' : clienteSelect.nome
    })
    
def delete(request, id):
    clienteSelect = get_object_or_404(Cliente, pk=id)
    clienteSelect.delete()
    
    return redirect(home)