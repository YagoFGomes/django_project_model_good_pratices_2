from django.urls import path

from .views import * 

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('cria_receita', cria_receita, name='cria_receita'),
    path('deletar/<int:receita_id>', deletar_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita'),
]