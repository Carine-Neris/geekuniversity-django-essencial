from django.contrib import admin
from .models import Cliente, Produtos


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'born_in_fifties')


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produtos, ProdutosAdmin)
