from django.contrib import admin
from .models import Category, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_display_links = ('product_name', 'price')
    list_filter = ('category', 'created_date', 'is_available')
    list_editable = ('is_available',)
    search_fields = ('product_name', 'category')
    ordering = ('product_name',)


admin.site.register(Product, ProductAdmin)


