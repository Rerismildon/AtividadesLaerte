from SegundaAtividade.models import *
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        
class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'