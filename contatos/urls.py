from django.urls.conf import include
from .views import ContatosView
from django.urls import path

urlpatterns = [
    path('', ContatosView.as_view(), name='home'),
    path('<int:contato_id>', ContatosView.as_view(), name='ver_contato')
]
