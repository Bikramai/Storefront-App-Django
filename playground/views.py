from django.shortcuts import render
from django.db import connection
from store.models import Order, OrderItem, Product, Customer, Collection


def say_hello(request):
    # queryset = Product.objects.raw('SELECT id, title FROM store_product') #use it only while dealing with complex query

    with connection.cursor() as cursor:
        cursor.execute()               #callproc('get_customers', [1, 2, 'a' ])
        
    return render(request, 'hello.html', {'name': 'Bikram', 'reault': list(connection)})
