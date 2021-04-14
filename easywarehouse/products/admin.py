from django.contrib import admin

from .models import Category, Image, Product


@admin.register(Product, Category, Image)
class ProductsAdmin(admin.ModelAdmin):
    pass
