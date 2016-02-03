from django.contrib import admin

# Register your models here.
from .models import *

class ProductImageInline(admin.TabularInline):
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


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(ProductImage)
admin.site.register(Order, OrderAdmin)



