from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'company')
