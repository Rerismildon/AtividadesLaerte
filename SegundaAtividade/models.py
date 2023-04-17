from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=500)
    telefone = models.CharField(max_length=20)
    dataNascimento = models.DateField()
    

