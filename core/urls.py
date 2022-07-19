from django.urls import path
from .views import index, contato,produto, teste


urlpatterns = [
    path('', index, name='index'),
    path('contatos', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    path('teste',teste, name='teste'),
]
