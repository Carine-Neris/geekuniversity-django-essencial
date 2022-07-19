from django.shortcuts import render
from .models import Cliente, Produtos


def index(request):
    itens = Produtos.objects.all()
    context = {
        'curso':'Programação web',
        'linguagem': 'Python',
        'produtos': itens
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def teste(request):
    print(request.headers)
    print(request.user)
    context = {
        'curso': 'Programação web',
        'linguagem': 'Python',
        'framework': 'Django'
    }
    return render(request, 'teste.html', context)


def produto(request, pk):
    item = Produtos.objects.get(id=pk)
    # O retorno de informações tem que sem no formato dict
    to_dict = {
        'nome': item.nome,
        'preco': item.preco,
        'quantidade': item.estoque
    }
    return render(request, 'produto.html',to_dict)