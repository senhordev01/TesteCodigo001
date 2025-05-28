from django.shortcuts import render, redirect
from .models import Dados, Produto
from django.contrib.auth.hashers import make_password, check_password
from .models import Produto, Pagamento
from .forms import PagamentoForm


def ver(request):
    if request.method == "POST":
        nome = request.POST.get('Nome')
        email = request.POST.get('Email')
        confirmar_email = request.POST.get('Confirmar_Email')
        senha = request.POST.get('Senha')
        confirmar_senha = request.POST.get('Confirmar_Senha')

        if email != confirmar_email or senha != confirmar_senha:
            return render(request, 'cadastro.html', {'erro': 'Erro na confirmação'})
        
        senha_criptografada = make_password(senha)
        Dados.objects.create(nome=nome, email=email, senha=senha_criptografada)

        return redirect('entrar_site')  # ou render(...)

    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        try:
            usuario = Dados.objects.get(email=email)
        except Dados.DoesNotExist:
            return render(request, 'login.html', {'erro': 'Email não encontrado'})
        
        if check_password(senha, usuario.senha):
            return redirect('site_primario')
        else:
            return render(request, 'login.html', {'erro': 'Senha incorreta'})

    return render(request, 'login.html')

def lista_produtos(request):
    produtos = Produto.objects.filter(estoque__gt=0, disponivel=True)
    return render(request, 'site.html', {'produtos': produtos})


# Create your views here.
def pagar_produto(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            
            produto = pagamento.produto  # produto relacionado no pagamento
            quantidade_comprada = pagamento.quantidade
            
            # Verifica se tem estoque suficiente
            if produto.estoque >= quantidade_comprada:
                produto.estoque -= quantidade_comprada
                produto.save()
                
                # Calcula total
                pagamento.total = produto.preco * quantidade_comprada
                pagamento.save()
                
                return redirect('pagamento_sucesso')
            else:
                form.add_error(None, 'Estoque insuficiente para esse produto.')
    else:
        form = PagamentoForm()

    # Este return deve estar fora do else, para funcionar no GET e caso POST seja inválido
    return render(request, 'metodo_pagamento.html', {'form': form})


def pagamento_sucesso(request):
    return render(request, 'pagamento_sucesso.html')


