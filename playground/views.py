from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem


def say_hello(request):
    #queryset = Product.objects.values_list('id', 'title', 'collection__title') 
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    
   

    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
