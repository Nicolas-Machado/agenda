from django.contrib import admin
from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobre_nome', 'email', 'data_criacao')
    list_display_links = ('id', 'nome')

admin.site.register(Contato, ContatoAdmin)
