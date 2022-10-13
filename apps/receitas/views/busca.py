from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    else:
        lista_receitas = ''

    receitas_a_exibir = {
        'receitas': lista_receitas
    }
    return render(request, 'receitas/buscar.html', receitas_a_exibir)
