from django.contrib import admin

from .models import Product, Variation


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_display_links = ('product_name', 'price')
    list_filter = ('category', 'created_date', 'is_available')
    list_editable = ('is_available',)
    search_fields = ('product_name', 'category')
    ordering = ('product_name',)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_display_links = ('product', 'variation_category', 'variation_value')
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')
    search_fields = ('product', 'variation_category', 'variation_value')
    list_editable = ('is_active',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)

