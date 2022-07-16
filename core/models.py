import email
from mailbox import NotEmptyError
from django.db import models
from django.forms import CharField

class Produtos(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)