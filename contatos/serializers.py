from rest_framework import serializers
from .models import Contato

class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        exclude = ('id', 'data_criacao')