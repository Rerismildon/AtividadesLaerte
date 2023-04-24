from django.shortcuts import redirect, render, get_object_or_404
from SegundaAtividade.models import Pedido
from SegundaAtividade.forms import PedidoForm

def home(request):
    Pedidos = Pedido.objects.all()       
    
    return render(request, 'Pedido/home.html', {
        "listaPedidos" : Pedidos,
    })
    
def insert(request):
    form = PedidoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('pedido.home')
    
    return render(request, 'Pedido/insert.html', {
        "form" : form,
    })
    
def edit(request, id):
    pedidoSelect = get_object_or_404(Pedido, pk=id)
    form = PedidoForm(request.POST or None, instance=pedidoSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('pedido.home')
    
    return render(request, 'Pedido/edit.html', {
        'form' : form,
        'nome' : id
    })
    
def delete(request, id):
    pedidoSelect = get_object_or_404(Pedido, pk=id)
    pedidoSelect.delete()
    
    return redirect(home)