from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.models import User
from receitas.models import Receita
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def index(request):

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    paginator = Paginator(receitas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_exibir = {
        'receita': receita
    }

    return render(request, 'receitas/receita.html', receita_exibir)

def cria_receita(request):

    if request.method == 'POST':
        
        nome = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita(pessoa=user,
                          nome_receita=nome,
                          ingredientes=ingredientes,
                          modo_preparo=modo_preparo,
                          tempo_preparo=tempo_preparo,
                          rendimento=rendimento,
                          categoria=categoria,
                          foto_receita=foto_receita)
        receita.save()

        return redirect('dashboard')

    else:
        return render(request, 'receitas/cria_receita.html')

def deleta_receita(request, receita_id):
    
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):

    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = { 'receita': receita }
    return render(request, 'receitas/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    
    if request.method == 'POST':
        
        receita_id = request.POST['receita_id']
        receita = Receita.objects.get(pk=receita_id)

        receita.nome_receita = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_preparo = request.POST['tempo_preparo']
        receita.rendimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']

        if 'foto_receita' in  request.FILES:
            receita.foto_receita = request.FILES['foto_receita']

        receita.save()

        return redirect('dashboard')
