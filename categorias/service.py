from .models import Categoria

class CategoriaService():
    def busca_todas_categorias(self):
        return Categoria.objects.all()
    