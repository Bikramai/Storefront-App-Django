from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # Products: inventory < 10 OR price < 20
    product = Product.objects.order_by('unit_price')[0]
    product = Product.objects.earliest('unit_price')

    return render(request, 'hello.html', {'name': 'Bikram', 'product': product})
