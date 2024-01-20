from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # 0, 1, 2, 3, 4
    # 5,6,7,8,9,10,11,12,13,14,
    queryset = Product.objects.all()[5:15]
   

    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
