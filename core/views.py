from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Cliente, Produtos


def index(request):
    itens = Produtos.objects.all()
    context = {
        'curso': 'Programação web',
        'linguagem': 'Python',
        'produtos': itens
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def teste(request):
    """https://docs.djangoproject.com/en/4.0/ref/request-response/"""
    print(dir(request))
    print(request.headers)
    print(request.user)
    print(request.method)
    print(request.scheme)
    print(request.body)
    print(request.path)
    context = {
        'curso': 'Programação web',
        'linguagem': 'Python',
        'framework': 'Django'
    }
    return render(request, 'teste.html', context)


def produto(request, pk):
    #item = Produtos.objects.get(id=pk)
    item = get_object_or_404(Produtos, id=pk)
    # O retorno de informações tem que sem no formato dict
    to_dict = {
        'nome': item.nome,
        'preco': item.preco,
        'quantidade': item.estoque
    }
    return render(request, 'produto.html', to_dict)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),
        content_type='text/html; charset=utf8',
        status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=500)


