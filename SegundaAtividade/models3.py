from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    dataNascimento = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
        
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco =  models.DecimalField(decimal_places=2, max_digits=32)
    estoque = models.IntegerField()
    descricao = models.CharField(max_length=2500)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
   
class Pedido(models.Model):
    dataPedido = models.DateField()
    dataEntregaPrevista = models.DateField() 
    dataEntregaReal = models.DateField(blank=True) 
    status = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.dataPedido}, R${self.valor}"
    
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

class Pagamento(models.Model):
    tipoPagamento = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    dataPagamento = models.DateField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)

class Compra(models.Model):
    idProduto = models.IntegerField()
    quantidade = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits=8, decimal_places=2)
    dataCompra = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    
class ItensPedidos(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)