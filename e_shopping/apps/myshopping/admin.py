from django.contrib import admin

# Register your models here.
from myshopping.models import (Category, Product, Cart, ProductImage, Order)
from users.models import (UserProfile , Relationship)

class ProductImageInline(admin.TabularInline):
    """To show Image with Product """
    model = ProductImage
    
    readonly_fields = ('image_tag',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("from_user", "product",
        "item_quantity","item_price", "product_purchas_date",
        "order_status","to_person")

    def has_add_permission(self, request, obj=None):
        return False

    def to_person(self, obj):
        to_users = obj.to_user.user.username
        return to_users


class ProductAdmin(admin.ModelAdmin):
    """docstring for ProductAdmin"""
    inlines = [
        ProductImageInline,
    ]

class CartAdmin(admin.ModelAdmin):
    list_display = ("from_user","product","creation_date","quantity","price")

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(ProductImage)
admin.site.register(Order, OrderAdmin)


