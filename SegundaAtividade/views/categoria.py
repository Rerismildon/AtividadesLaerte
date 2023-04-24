from django.shortcuts import redirect, render, get_object_or_404
from SegundaAtividade.models import Categoria
from SegundaAtividade.forms import CategoriaForm

def home(request):
    Categorias = Categoria.objects.all()       
    
    return render(request, 'Categoria/home.html', {
        "listaCategorias" : Categorias,
    })
    
def insert(request):
    form = CategoriaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('categoria.home')
    
    return render(request, 'Categoria/insert.html', {
        "form" : form,
    })
    
def edit(request, id, nome):
    categoriaSelect = get_object_or_404(Categoria, pk=id)
    form = CategoriaForm(request.POST or None, instance=categoriaSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('categoria.home')
    
    return render(request, 'Categoria/edit.html', {
        'form' : form,
        'nome' : nome
    })
    
def delete(request, id):
    categoriaSelect = get_object_or_404(Categoria, pk=id)
    categoriaSelect.delete()
    
    return redirect(home)