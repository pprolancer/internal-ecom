from django.db import models
from sorl.thumbnail import ImageField
from django.core.validators import MinValueValidator
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

class ShoppingCart(models.Model):
    product = models.ForeignKey("Product", related_name='product')
    product_count = models.IntegerField(blank=True, null=True)
    product_price_limit = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCart"

    def __str__(self):
        return self.product_count