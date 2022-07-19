from django.urls import path
from .views import index, contato,produto, teste


urlpatterns = [
    path('', index),
    path('contatos', contato),
    path('produto/<int:pk>', produto, name='produto'),
    path('teste',teste),
]
