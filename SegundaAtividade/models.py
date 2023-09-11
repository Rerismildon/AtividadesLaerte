from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from SegundaAtividade.validators import data_menor_atual, data_menor_igual_atual, numero, EscolhaValidator

class Usuario(models.Model):
    nome_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                       MaxLengthValidator(100, "Maximo de 100 digitos.")]  
    senha_validators = [MinLengthValidator(8, "Minimo de 8 digitos."),
                           MaxLengthValidator(50, "Maximo de 100 digitos.")]

    nome = models.CharField(max_length=100, validators=nome_validators)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=20, validators=senha_validators)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                       MaxLengthValidator(100, "Maximo de 100 digitos.")]
    datanasc_validators = [data_menor_atual]
    telefone_validators = [numero("Telefone"),
                           MinLengthValidator(8, "Minimo de 8 digitos."),
                           MaxLengthValidator(15, "Maximo de 15 digitos.")]

    nome  = models.CharField(max_length=100, validators=nome_validators)
    email = models.EmailField(max_length=1000, unique=True)
    dataNascimento = models.DateField(validators=datanasc_validators)
    telefone = models.CharField(max_length=15, validators=telefone_validators) 
    usuario = models.OneToOneField('Usuario', on_delete=models.SET_NULL, null=True,blank=True, related_name='cliente')

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome_validadors = [MinLengthValidator(2, "Minimo de 2 digitos."),
                       MaxLengthValidator(50, "Maximo de 50 digitos.")]
    
    desc_validators = [MinLengthValidator(10, "Minimo de 10 digitos."),
                       MaxLengthValidator(500, "Maximo de 50 digitos.")]
    
    nome  = models.CharField(max_length=100, validators=nome_validadors)
    descricao = models.CharField(max_length=500, validators=desc_validators)

    def __str__(self):
        return self.nome
    
class Fornecedor(models.Model):
    nome_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                       MaxLengthValidator(100, "Maximo de 100 digitos.")] 
    endereco_validators = [MinLengthValidator(5, "Minimo de 5 digitos."),
                       MaxLengthValidator(200, "Maximo de 200 digitos.")]
    telefone_validators = [numero("Telefone"),
                           MinLengthValidator(8, "Minimo de 8 digitos."),
                           MaxLengthValidator(15, "Maximo de 100 digitos.")]   

    nome = models.CharField(max_length=100, validators=nome_validators)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(unique=True, validators=endereco_validators)
    telefone = models.CharField(max_length=15, validators=telefone_validators)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                       MaxLengthValidator(100, "Maximo de 100 digitos.")]
    desc_validators = [MinLengthValidator(10, "Minimo de 10 digitos."),
                       MaxLengthValidator(500, "Maximo de 100 digitos.")]
    preco_validators = [MinValueValidator(0.01, "De graça não né.")]    
    estoque_validators = [MinValueValidator(0, "Estoque vazio?.")]

    nome = models.CharField(max_length=1000, validators=nome_validators)
    descricao = models.CharField(max_length=1000, validators=desc_validators)
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=preco_validators)
    estoque = models.IntegerField(default=0,null=True, validators=estoque_validators)
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING, null=True, related_name='produtos')
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.DO_NOTHING,null=True,  related_name='produtos', blank=True)

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    nome_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                       MaxLengthValidator(100, "Maximo de 100 digitos.")] 
    cargo_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                       MaxLengthValidator(50, "Maximo de 50 digitos.")]
    telefone_validators = [numero("Telefone"),
                           MinLengthValidator(8, "Minimo de 8 digitos."),
                           MaxLengthValidator(15, "Maximo de 50 digitos.")]
    
    nome = models.CharField(max_length=100, validators=nome_validators)
    cargo = models.CharField(max_length=20, validators=cargo_validators)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, validators=telefone_validators)

    def __str__(self) -> str:
        return f"{self.nome}, {self.cargo}"

class Pedido(models.Model):
    data_validators = [data_menor_igual_atual]
    data_entrega_real_validators = [data_menor_igual_atual]
    status_validators = [EscolhaValidator(["Em aberto", "Em andamento", "Finalizado"])]
    valor_total_validators = [MinValueValidator(0.01, "0???.")]

    dataPedido = models.DateField(null=True, blank=True)
    dataEntregaPrevista = models.DateField()
    dataEntregaReal = models.DateField(null=True, blank=True, validators=data_entrega_real_validators)
    status = models.CharField(max_length=20, validators=status_validators)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=valor_total_validators)
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, related_name='pedidos')

    def __str__(self):
        return f"{self.data}, R${self.valor_total}"

class Endereco(models.Model):
    rua_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                      MaxLengthValidator(100, "Maximo de 100 digitos.")]
    
    numero_validators = [numero("Número"),
                         MaxLengthValidator(10, "Maximo de 10 digitos.")]
    
    bairro_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                      MaxLengthValidator(50, "Maximo de 50 digitos.")]
    
    cidade_validators = [MinLengthValidator(2, "Minimo de 2 digitos."),
                      MaxLengthValidator(50, "Maximo de 50 digitos.")]

    estado_validators = [MinLengthValidator(2, "Exatamente 2 digitos.")]

    cep_validators = [numero("Cep"),
                      MinLengthValidator(8, "Exatamente 8 digitos.")]

    rua = models.CharField(max_length=100, validators=rua_validators)
    numero = models.CharField(max_length=10, validators=numero_validators)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50, validators=bairro_validators)
    cidade = models.CharField(max_length=50, validators=cidade_validators)
    estado = models.CharField(max_length=2, validators=estado_validators)
    cep = models.CharField(max_length=8, validators=cep_validators)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.rua}, n°{self.numero}"

class Pagamento(models.Model):
    tipo_validators = [EscolhaValidator(["Cartão de crédito", "Boleto", "Transferência bancária"])]
    valor_validators = [MinValueValidator(0.01, "Valor deve ser maior que 0.")]
    data_validators = [data_menor_atual]

    tipoPagamento = models.CharField(max_length=50, validators=tipo_validators)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=valor_validators)
    dataPagamento = models.DateField(validators=data_validators)
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.tipo}, R${self.valor}"
    
class Compra(models.Model):
    quantidade_validators = [MinValueValidator(1, "Nenhum item kkk?.")]
    preco_validators = [MinValueValidator(1*10**-2, "Dea graça não né.")]

    idProduto = models.IntegerField()
    quantidade = models.IntegerField(validators=quantidade_validators)
    precoUnitario = models.DecimalField(max_digits=10, decimal_places=2, validators=preco_validators)
    dataCompra = models.DateField()
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, related_name='compras')

class ItensPedidos(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, related_name='itensPedidos')
    produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING, related_name='pedidos')
    quantidade = models.IntegerField()





