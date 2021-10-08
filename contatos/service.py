from django.db.models.functions import Concat
from django.db.models import Q, Value

from categorias.models import Categoria
from.models import Contato


def buscar_todos_contatos():
    return Contato.objects.all().filter(
        ativo=True
    )


def buscar_contatos_por_id(id: int) -> Contato:
    return Contato.objects.filter(id=id).first()


def buscar_contatos_por_termo(termo: str):
    campos = Concat('nome', Value(' '), 'sobre_nome')
    return Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(sobre_nome__icontains=termo),
        ativo=True,
    )

def editar_contato_por_id(id:int, data:dict):
    return Contato.objects.filter(id=id).update(**data)

def editar_contato_by_id(id:int, data:dict):
    return Contato.objects.filter(id=id).update(**data)


def editar_contato(contato:Contato, data:dict, categoria:Categoria) -> None:
    contato.nome = data['nome']
    contato.sobre_nome = data['sobre_nome']
    contato.telefone = data['telefone']
    contato.email = data['email']
    contato.categoria = categoria
    contato.save()

def remover_contatos_por_id(id: int) -> int:
    return Contato.objects.filter(id=id).delete()
