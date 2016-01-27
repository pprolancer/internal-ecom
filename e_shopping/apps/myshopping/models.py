from django.db import models
from sorl.thumbnail import ImageField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Category(models.Model):
    title = models.CharField("Title",max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey("Category", related_name='category')
    product_name = models.CharField("Product Name", max_length=100)
    product_price = models.CharField("Product Price", max_length=100)
    product_description = models.CharField("Product Description",max_length=225)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey("Product", related_name ='productcart')
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.CharField("Quantity", max_length=100)
    price = models.CharField("Product cart Price", max_length=100)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def add(self,user,product,price,quantity):
        cart, created = Cart.objects.get_or_create(user=user,
            product=product,price=price, quantity= quantity)
        cart.save()
        return True

    # def remove 
