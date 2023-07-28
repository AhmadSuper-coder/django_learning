from django.contrib import admin
from .models import Product, ProductItem,Category
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','description', 'price', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'sku', 'quantity', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('product__name', 'sku')
    date_hierarchy = 'created_at'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at')
    list_filter = ('parent',)
    search_fields = ('name',)


