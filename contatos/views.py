from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from . import service
from django.core.paginator import Paginator

import contatos


class ContatosView(APIView):
    def get(self, request, contato_id=None):
        if contato_id is None:
            contatos = service.buscar_todos_contatos()
            paginator = Paginator(contatos, 3)
            page = request.GET.get('p')
            contatos = paginator.get_page(page)
            return render(request=request, template_name='home.html', context={'contatos': contatos})

        contato = service.buscar_contatos_por_id(contato_id)
        return render(request=request, template_name='contato.html', context={'contato': contato})


class ContatosBuscaView(APIView):
    def get(self, request):
        termo = request.GET.get('termo')
        contatos = service.buscar_contatos_por_termo(termo)
        paginator = Paginator(contatos, 3)
        page = request.GET.get('p')
        contatos = paginator.get_page(page)
        return render(request=request, template_name='home.html', context={'contatos': contatos})
