"""
Custumização da paginação do admin. 
Códigos nos site:

https://hakibenita.com/optimizing-the-django-admin-paginator
"""
from django.db import connection, transaction, OperationalError
from functools import cached_property
from django.core.paginator import Paginator


class PaginatorCostumizado(Paginator):


    @cached_property
    def count(self):
        return 9999999999


# Está implementação só funciona em bancos como mysql e postgresql. o sql não
# imlementa esse timeout
class TimeLimitedPaginator(Paginator):
    """
    Paginator that enforces a timeout on the count operation.
    If the operations times out, a fake bogus value is
    returned instead.
    """
    @cached_property
    def count(self):
        # We set the timeout in a db transaction to prevent it from
        # affecting other transactions.
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.execute('SET LOCAL statement_timeout TO 200;')
            try:
                return super().count
            except OperationalError:
                return 9999999999
