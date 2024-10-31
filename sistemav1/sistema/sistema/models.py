from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    cpf = models.CharField(
        max_length=11,  
        null=False,
        blank=False 
    )
    
    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    
    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

class Usuario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False
    )
    
    senha = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )
    

objetos = models.Manager()
   

