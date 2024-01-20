from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem


def say_hello(request):
    queryset = Product.objects.defer('description') 
    
   

    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
