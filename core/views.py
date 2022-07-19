from django.shortcuts import render


def index(request):
    print(request.headers)
    print(request.user)
    context = {
        'curso':'Programação web',
        'linguagem': 'Python',
        'framework': 'Django'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
