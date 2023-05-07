from django.shortcuts import redirect, render, get_object_or_404
from meuapp.models import Pagamento
from meuapp.forms import PagamentoForm

def home(request):
    pagamentos = Pagamento.objects.all()       
    
    return render(request, 'Pagamento/home.html', {
        "listaPagamentos" : pagamentos,
    })
    
def insert(request):
    form = PagamentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('pagamento.home')
    
    return render(request, 'Pagamento/insert.html', {
        "form" : form,
    })
    
def edit(request, id, nome):
    pagamentoSelect = get_object_or_404(Pagamento, pk=id)
    form = PagamentoForm(request.POST or None, instance=pagamentoSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('pagamento.home')
    
    return render(request, 'Pagamento/edit.html', {
        'form' : form,
        'nome' : nome
    })
    
def delete(request, id):
    pagamentoSelect = get_object_or_404(Pagamento, pk=id)
    pagamentoSelect.delete()
    
    return redirect('pagamento.home')
