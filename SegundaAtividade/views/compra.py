from django.shortcuts import redirect, render, get_object_or_404
from meuapp.models import Compra
from meuapp.forms import CompraForm

def home(request):
    compras = Compra.objects.all()       
    
    return render(request, 'Compra/home.html', {
        "listaCompras" : compras,
    })
    
def insert(request):
    form = CompraForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('compra.home')
    
    return render(request, 'Compra/insert.html', {
        "form" : form,
    })
    
def edit(request, id, nome):
    compraSelect = get_object_or_404(Compra, pk=id)
    form = CompraForm(request.POST or None, instance=compraSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('compra.home')
    
    return render(request, 'Compra/edit.html', {
        'form' : form,
        'nome' : nome
    })
    
def delete(request, id):
    compraSelect = get_object_or_404(Compra, pk=id)
    compraSelect.delete()
    
    return redirect('compra.home')
