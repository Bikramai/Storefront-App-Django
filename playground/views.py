from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # Products: inventory < 10 OR price < 20
    queryset = Product.objects.filter(
        Q(inventory__lt=10) | Q(unit_price__lt=20))

    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
