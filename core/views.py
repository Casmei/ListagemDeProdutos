from django.shortcuts import render
from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    if request.user == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = str(request.user).title()
        
    context = {
        'apresentacao': 'Olá, eu me chamo Tiago',
        'logado': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #Vai pegar o objeto que tem o Id igual o Pk
    prod = Produto.objects.get(id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
