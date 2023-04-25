from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=500)
    telefone = models.CharField(max_length=20)
    dataNascimento = models.DateField()

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco =  models.DecimalField(decimal_places=2, max_digits=32)
    estoque = models.IntegerField()
    descricao = models.CharField(max_length=2500)
   
class Pedido(models.Model):
    dataPedido = models.DateField()
    dataEntregaPrevista = models.DateField() 
    dataEntregaReal = models.DateField(blank=True) 
    status = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=10)

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=1000)
    
class Fornecedor(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
