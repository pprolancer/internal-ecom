from django.contrib import admin

# Register your models here.
from myshopping.models import (Category, Product, Cart, ProductImage, Order)
from users.models import (UserProfile , Relationship)

class ProductImageInline(admin.TabularInline):
    """To show Image with Product """
    model = ProductImage
    
    readonly_fields = ('image_tag',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "item_quantity","item_price", "product_purchas_date", "order_status")

    def has_add_permission(self, request, obj=None):
        return False

class ProductAdmin(admin.ModelAdmin):
    """docstring for ProductAdmin"""
    inlines = [
        ProductImageInline,
    ]

# class UserProfileInline(admin.TabularInline):
#     """To show Image with Product """

#     model = UserProfile
#     readonly_fields = ('user_role',)

# class CartAdmin(admin.ModelAdmin):
#     list_display = ("user","user_role", "product", "quantity","price")
    # inlines = [
    #     UserProfileInline,
    # ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(ProductImage)
admin.site.register(Order, OrderAdmin)



