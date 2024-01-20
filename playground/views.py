from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # select_related(1)
    # prefetch_related (n)
    queryset = Product.objects.prefetch_related(
        'promotions').select_related('collection').all()

    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})


# Exercise
# Get the last 5 orders with their customer
# and items (include product)
# def say_hello(request):
#     # select_related(1)
#     # prefetch_related (n)
#     queryset = Order.objects.select_relatede(
#         'customer').order_by('-placed_at')[:5]

#     return render(request, 'hello.html', {'name': 'Bikram', 'orders': list(queryset)})
