from django.shortcuts import redirect, render, get_object_or_404
from SegundaAtividade.models import ItensPedidos
from SegundaAtividade.forms import ItensPedidosForm

def home(request):
    itenspedidos = ItensPedidos.objects.all()       
    
    return render(request, 'ItensPedidos/home.html', {
        "listaItensPedidos" : itenspedidos,
    })
    
def insert(request):
    form = ItensPedidosForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('itenspedidos.home')
    
    return render(request, 'ItensPedidos/insert.html', {
        "form" : form,
    })
    
def edit(request, id):
    itempedidoSelect = get_object_or_404(ItensPedidos, pk=id)
    form = ItensPedidosForm(request.POST or None, instance=itempedidoSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('itenspedidos.home')
    
    return render(request, 'ItensPedidos/edit.html', {
        'form' : form,
        'nome' : "ItemPedido"
    })
    
def delete(request, id):
    itempedidoSelect = get_object_or_404(ItensPedidos, pk=id)
    itempedidoSelect.delete()
    
    return redirect('itenspedidos.home')
