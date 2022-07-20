from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Produtos(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')


    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    @admin.display(boolean=True)
    def born_in_fifties(self):
        return True

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    