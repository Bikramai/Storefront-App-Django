from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 15


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 15



# Register your models here.
admin.site.register(models.Collection)


# admin.site.register(models.Product, ProductAdmin) # we donot need this line because we put decorate that is the best way to practise