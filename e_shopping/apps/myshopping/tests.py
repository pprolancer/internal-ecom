from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from myshopping.models import Category, Product, Cart


class CategoryTestCase(TestCase):
    fixtures = ["tests.json"]

    def setUp(self):
        super(CategoryTestCase, self).setUp()
        self.category_1 = Category.objects.get(pk=1)
        self.category_2 = Category.objects.get(pk=2)

    def test_pass_stringification(self):
        """
        Test the stringification of a ``User`` object. A
        "human-readable" representation of an ``User`` object.
        """
        category_name_1 = self.category_1.title
        self.assertEqual(self.category_1.__str__(), category_name_1, "USER STRING METHOD WORK")

    def test_fail_stringification(self):
        """
        Test the stringification of a ``User`` object. A
        "human-readable" representation of an ``User`` object.
        """

        category_name_2 = self.category_2.title
        self.assertEqual(self.category_2.__str__(), category_name_2, "USER STRING METHOD NOT WORK")


class ProductTestCase(TestCase):
    fixtures = ["tests.json"]

    def setUp(self):
        super(ProductTestCase, self).setUp()
        self.product_1 = Product.objects.get(pk=1)
        self.product_2 = Product.objects.get(pk=2)

    def test_pass_stringification(self):
        """
        Test the stringification of a ``Product`` object. A
        "human-readable" representation of an ``Product`` object and check correct value for field.
        """
        product_name_1 = self.product_1.product_name
        self.assertEqual(self.product_1.__str__(), product_name_1, "PRODUCT STRING METHOD WORK")

        product_product_price_1 = self.product_1.product_price
        self.assertEqual(self.product_1.product_price.format(), product_product_price_1, "PRODUCT STRING METHOD NOT WORK")

        product_product_description_1 = self.product_1.product_description
        self.assertEqual(self.product_1.product_description.format(), product_product_description_1, "PRODUCT STRING METHOD NOT WORK")


    def test_fail_stringification(self):
        """
        Test the stringification of a ``Product`` object. A
        "human-readable" representation of an ``Product`` object and check correct value for field.
        """

        product_name_2 = self.product_2.product_name
        self.assertEqual(self.product_2.__str__(), product_name_2, "PRODUCT STRING METHOD NOT WORK")

        product_product_price_2 = self.product_2.product_price
        self.assertEqual(self.product_2.product_price.format(), product_product_price_2, "PRODUCT STRING METHOD NOT WORK")

        product_product_description_2 = self.product_2.product_description
        self.assertEqual(self.product_2.product_description.format(), product_product_description_2, "PRODUCT STRING METHOD NOT WORK")

 
