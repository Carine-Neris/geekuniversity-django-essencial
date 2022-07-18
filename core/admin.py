import site
from django.contrib import admin

from .models import Cliente, Produtos


admin.site.register(Cliente)
admin.site.register(Produtos)
