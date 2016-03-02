from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from myshopping.models import Category, Product, Cart, ProductImage
from django.contrib.auth.models import User
from users.models import UserProfile
from django.test import Client
import datetime
from django.utils.crypto import get_random_string


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

    def test_valid_product_price(self):
        """Test Cases To check Price Type """
        product = Product.objects.get(pk=1)
        price = product.product_price
        if isinstance(price, str):
            print("Invalid Product Price")
        elif not isinstance(float(price), float):
            print("Invalid Product Price")
        elif float(price) < 0:
            print("Invalid Product Price")
        else:
            print("Valid Product Price")

    def test_check_valid_category(self):
        """Test Cases To check Valid Category """ 
        product = Product.objects.get(pk=1)
        category = Category.objects.get(pk=1)
        self.assertEqual(product.category, category, "Valid Category") 



class CartTestCase(TestCase):
    """ TEST FOR CART """
    fixtures = ["tests.json"]
    def setup(self):
        super(CartTestCase, self).setup()
        self.client = Client()

    def _create_dummy_cart(self, item = '', from_user = '', to_user = '',price = 100, creation_date = datetime.datetime.now(), quantity = 1):
        cart = Cart()
        cart.from_user = from_user
        cart.to_user = to_user
        cart.product = item
        cart.creation_date = creation_date
        cart.quantity = quantity
        cart.price = price * quantity
        cart.product_id = item.id
        cart.save()
        return cart

    def _create_dummy_item(self, category='', price = 100):
        product = Product()
        product.category = category
        product.product_name = "Mobile"
        product.product_price = price
        product.product_description = "Mobile"
        product.save()
        return product

    def _create_dummy_user(self, username = '',user_role = ''):
        user = User()
        user.username = username+str(get_random_string(length=5))
        user.first_name = "John"
        user.last_name = "john"
        user.set_password("12345678@")
        user.save()

        userprofile = UserProfile(user=user)
        userprofile.user_role = user_role
        userprofile.product_count = 10
        userprofile.product_price_limit = 100
        userprofile.birth_date = datetime.datetime.now()
        userprofile.save()
        return userprofile

    def test_cart_creation(self):
        """ TEST CREATE CART AND CHECK IS EQUAL TO THE CREATED CART AND THE CART GET FROM DATABASE """
        creation_date = datetime.datetime.now()
        category = Category.objects.get(pk=1)
        item = self._create_dummy_item(category=category, price = 100)
        from_user = self._create_dummy_user('yogesh','parent')
        to_user = self._create_dummy_user('john','student')
        cart = self._create_dummy_cart(item, from_user, to_user, price = 100, creation_date = datetime.datetime.now())
        id = cart.id
        cart_from_database = Cart.objects.get(pk=id)
        self.assertEquals(item.id,cart_from_database.product_id, "Valid Product In cart")

    
    def test_item_creation_and_association_with_cart(self):
        """ enable USER to associate an item in the cart with product model """        
        
        category = Category.objects.get(pk=1)
        item = self._create_dummy_item(category=category, price = 100)

        from_user = self._create_dummy_user('yogesh','parent')
        to_user = self._create_dummy_user('john','student')
        cart = self._create_dummy_cart(item, from_user, to_user, price = 100, creation_date = datetime.datetime.now())
        item_in_cart = Cart.objects.all()[0]

        self.assertEquals(item_in_cart.price, item.product_price, "Unit price of the first item stored in the cart should equal 100")
        self.assertEquals(item_in_cart.quantity, 1, "The first item in cart should have 1 in it's quantity")

    def test_total_item_price(self):
        """ CHECK TOTAL PRICE OF ITEMS IN CART """
        from_user = self._create_dummy_user('yogesh','parent')
        to_user = self._create_dummy_user('john','student')
        category = Category.objects.get(pk=1)
        item = self._create_dummy_item(category=category, price = 100)
        cart = self._create_dummy_cart(item, from_user, to_user, price = 100, creation_date = datetime.datetime.now(), quantity = 3)
        self.assertEquals(cart.price, 300, "Price should be equal to the multiplication of price and quantity!")

    def test_update_cart(self):
        """ CHECK CARTUPDATE """
        from_user = self._create_dummy_user('yogesh','parent')
        to_user = self._create_dummy_user('john','student')

        category = Category.objects.get(pk=1)
        item = self._create_dummy_item(category=category, price = 100)
        cart = self._create_dummy_cart(item, from_user, to_user, price = 100, creation_date = datetime.datetime.now(), quantity = 3)
        updated_quantity = 5
        Cart.objects.filter(product_id=cart.product_id, from_user=from_user,to_user=to_user).update(quantity=updated_quantity, price = item.product_price*updated_quantity)
        cart1 = Cart.objects.get(product_id=cart.product_id, from_user=from_user, to_user=to_user)
        self.assertEquals(cart1.price, item.product_price*updated_quantity, "Price should be equal to the multiplication of price and updated quantity!")
