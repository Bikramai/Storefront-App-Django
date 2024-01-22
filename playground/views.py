from django.shortcuts import render
from store.models import Order, OrderItem, Product, Customer, Collection
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()

    

    return render(request, 'hello.html', {'name': 'Bikram'})
