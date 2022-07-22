from django.contrib import admin
from .models import Cliente, Produtos


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'born_in_fifties')


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    search_fields = ('nome',)

    #implementação para buscar estoque
    #ModelAdmin.get_search_results( request , queryset , search_term )
    def get_search_results(self, request, queryset, search_term):
        print(request)
        print(queryset.values())
        print(search_term)
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term,
        )
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(estoque=search_term_as_int)
        print(queryset.values())
        return queryset, may_have_duplicates

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produtos, ProdutosAdmin)
