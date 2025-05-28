from django.contrib import admin
from .models import Produto, Dados, Pagamento, Produto
# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'disponivel')
    list_editable = ('preco', 'estoque')

@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    list_editable = ('email', 'senha')
    search_fields = ('nome', 'email')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'descricao')
    list_editable = ('preco', 'estoque')

@admin.register(Pagamento)
class Pagamento(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'total', 'data')