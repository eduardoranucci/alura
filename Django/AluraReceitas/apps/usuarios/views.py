from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

# Create your views here.

def cadastro(request):
    ''' Cadastra um novo usuário no sistema '''

    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode estar vazio.')
            return redirect('cadastro')
        elif campo_vazio(email):
            messages.error(request, 'O campo email não pode estar vazio.')
            return redirect('cadastro')
        elif senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não conferem.')
            return redirect('cadastro')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return redirect('cadastro')
        elif User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome de usuário já existente.')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login')

    else:    
        return render(request, 'usuarios/cadastro.html')

def login(request):
    ''' Realiza o login de um usuário no sistema '''

    if request.method == 'POST':

        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            
            messages.error(request, 'Os campos email e senha não podem ser vazios.')
            return redirect('login')
        
        elif User.objects.filter(email=email).exists():
            
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                
                auth.login(request, user)
                return redirect('dashboard')
        else:
            return redirect('login')
    
    else:
        return render(request, 'usuarios/login.html')

def dashboard(request):
    ''' Renderiza a dashboard do usuário '''

    if request.user.is_authenticated:

        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    ''' Realiza o logout de um usuário '''

    auth.logout(request)
    return redirect('index')

def campo_vazio(campo):
    ''' Verifica se um campo é vazio '''

    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    ''' Verifica se as senhas não são iguais '''

    return senha != senha2
