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
        
class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'




class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'