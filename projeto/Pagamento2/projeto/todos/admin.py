from django.contrib import admin
from .models import Produto, Pagamento

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'descricao')
    list_editable = ('preco', 'estoque')

@admin.register(Pagamento)
class Pagamento(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'total', 'data')