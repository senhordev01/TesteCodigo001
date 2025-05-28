from django.urls import path
from . import views

urlpatterns = [
    path('pagar/', views.pagar_produto, name = "pagar_produto"),
    path('pagamento_sucesso/', views.pagamento_sucesso, name="pagamento_sucesso")
]
