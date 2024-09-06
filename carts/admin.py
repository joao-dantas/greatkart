from django.contrib import admin

# Register your models here.

from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
