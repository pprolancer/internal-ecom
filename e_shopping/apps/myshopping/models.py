from django.db import models
from sorl.thumbnail import ImageField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime
from auditlog.registry import auditlog
import uuid
import os
from decimal import Decimal
from users.models import UserProfile
# Create your models here.

ORDER_STATUS = (
('Pending','PENDING'),
('Processed','PROCESSED'),
('Returned','RETURNED'),
('Canceled','CANCELED'),
)

def file_name(instance, filename):
    name, ext = os.path.splitext(filename)
    name_uuid = uuid.uuid1().__str__()
    return ''.join([name_uuid, ext])

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

    @property
    def product_image(self):
        images= self.productimage.all()
        image = images and images[0] or False
        return  image


class Cart(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey("Product", related_name ='productcart')
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.IntegerField("Quantity", default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def add(self,user,product,price,quantity):
        try:
            cart, created = Cart.objects.get_or_create(user=user,
                product=product,price=price, quantity= quantity)
            cart.save()
        except:
            pass
        return True


    # def user_name(self):
    #     import pdb;pdb.set_trace()
    #     return self.user.user



class ProductImage(models.Model):
    product = models.ForeignKey("Product", related_name ='productimage')
    image = models.ImageField(
        "Photo", upload_to=file_name, blank=True, null=True)

    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"

    def image_tag(self):
        return u'<img src="%s" height="100px" width="100px"/>' % self.image.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Order(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey("Product", related_name ='order_product')
    product_purchas_date = models.DateTimeField(auto_now_add=True, blank=True)
    item_quantity = models.IntegerField("Item Order Quantity", default=0)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)#default=Decimal(0.0)
    order_status = models.CharField(
        "User Order Status", max_length=50, choices=ORDER_STATUS)
    class Meta:
        verbose_name = "Orders"
        verbose_name_plural = "Orders"