from django.urls.conf import include
from .views import ContatosView, ContatosBuscaView, cadastroUsuario, contatosEditarView, contatosExcluirView
from django.urls import path

urlpatterns = [
    path('', ContatosView.as_view(), name='home'),
    path('<int:contato_id>', ContatosView.as_view(), name='ver_contato'),
    path('busca/', ContatosBuscaView.as_view(), name='busca'),
    path('cadastro/', cadastroUsuario.as_view(), name='cadastro'),
    path('deletar/<int:contato_id>', contatosExcluirView.as_view(), name='deletar'),
    path('editar/<int:contato_id>', contatosEditarView.as_view(), name='editar'),
    path('editar/salvar/', contatosEditarView.as_view(), name='editar_salvar'),
]
