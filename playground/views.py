from django.shortcuts import render
from store.models import Order, OrderItem, Product, Customer, Collection
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection(pk=11)
    collection.delete() #deleting only one object


    Collection.objects.filter(id__gt=5).delete() #deleteing multiple objects 



    return render(request, 'hello.html', {'name': 'Bikram'})
