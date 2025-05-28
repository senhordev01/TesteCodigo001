from django.shortcuts import render, redirect
from .models import Produto, Pagamento
from .forms import PagamentoForm


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
