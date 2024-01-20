from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # Products: inventory < 10 OR price < 20
    queryset = Product.objects.filter(inventory=F('collection__id'))

    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
