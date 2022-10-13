from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    """ Cadastra uma nova pessoa no sistema """

    if request.method == 'POST':
        
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco!')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request,'O campo email não pode ficar em branco!')
            return redirect('cadastro')

        if campo_vazio(senha):
            messages.error(request, 'O campo senha não pode ficar em branco!')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas devem ser iguais!')
            return redirect('cadastro')
        
        if User.objects.filter(username=nome).exists():
            messages.error(request,'Username já cadastrado!')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email de usuário já cadastrado!')
            return redirect('cadastro')
        
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """ Realiza o login de uma pessoa no sistema """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos não podem ficar em branco.')
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso!')
                return redirect('dashboard')

        return redirect('usuarios/login.html')

    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=request.user.id)
        context = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', context)
    else:
        return redirect('index')

def campo_vazio(campo):
    """ Verifica se o campo do formulário informado está vazio """
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
