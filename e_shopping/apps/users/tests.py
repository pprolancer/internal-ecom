from django.test import TestCase
from django.conf import settings
# Create your tests here.
from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
from django.test import Client
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django import forms
from .forms import RegistrationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import string

class UserTestCase(TestCase):
    """BASIC TESTS"""
    fixtures = ["tests.json"]
    def setUp(self):
        super(UserTestCase, self).setUp()
        self.user_1 = User.objects.get(pk=1)
        self.user_2 = User.objects.get(pk=2)

    def test_pass_stringification(self):
        """
        TEST FOR VALID USER, THE DATA GET FROM DATABASE AND THE DATA GET FROM CLIENT SIDE(ASSUME FROM TESTS.JSON) SHOULD BE EQUAL.
        """
        user2 = self.user_2.username
        self.assertEqual(self.user_2.__str__(), user2, "USER STRING METHOD WORK")

    def test_existing_user_update(self):
        """
        TEST FOR UPDATE THE EXISTING USER
        """
        user2 = User.objects.get(pk=2)
        user2.username = "gautam"
        user2.save()

    def test_create_new_user(self):
        """
        TEST FOR UPDATE THE EXISTING USER WITH ALL FIELDS
        """
        user = User.objects.get(pk=2)
        user.username = "rohit"
        user.first_name = "Rohit"
        user.last_name = "Raaj"
        user.password = "password"
        user.save()

    # def test_User_Login(self):
    #   """ TEST USER LOGIN """
    #     print(User.objects.all())
    #     response = self.client.post('/register/',{
    #         'email': 'user@example.com',
    #         'first_name': 'John',
    #         'password1': 'password',
    #         'password2': 'password',
    #     })
    #     print(User.objects.all()) # returns one user
    #     print(User.objects.all()[0].is_authenticated()) # returns True

    def test_check_unique_username(self):
        """ TEST unique username """
        user = User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
        if User.objects.filter(username='john').count():
            print("username already exists")

    def test_check_unique_email(self):
        """ TEST unique email """
        user = User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
        if User.objects.filter(email='jlennon@beatles.com').count():
            print("Email already exists")



    # def test_check_valid_email(self):
    #   self.f = forms.EmailField()
    #   email = "manisha.k@cisinlabs.com"
    #   self.assertRaises(ValidationError, self.f.clean(email), "INVALID EMAIL")


    def test_check_valid_first_name(self):
        """TEST VALID FIRST NAME"""
        first_name = "kumar gautam"
        if(first_name.find(' ')):
            print("Invalid First Name")
        else:
            print("Valid first name")

    def test_check_valid_last_name(self):
        """ TEST VALID LAST NAME """
        first_name = "yogesh"
        if(first_name.find(' ')):
            print("Invalid Last Name")
        else:
            print("Valid Last name")

    def test_check_valid_password_length(self):
        password = "Password"
        if len(password) >= 8:
            print("Valid Password")

    def test_check_invalid_password_length(self):
        """ TEST VALID PASSWORD WITH LENGTH """
        password = "abcd"
        if len(password) < 8:
            print("Invalid Password")

    def test_check_password_match_or_not(self):
        """ TEST FOR PASSWORD MATCH """
        password1 = "password1"
        password2 = "sdfsd"
        if not password2:
            print("You must enter confirm password")
        if password1 != password2:
            print("Your passwords do not match")

    def test_check_password_numeriacal_pattern(self):
        """ TEST FOR PASSWORD NOT EQUAL TO CONTINUE NUMERIC NUMBER """
        password = "12345678"
        str1 = "".join(str(x) for x in range(1,21))
        if password in str1:
            print("Most common password")

    def test_check_password_alphabetic_lowercase_pattern(self):
        """ TEST FOR PASSWORD NOT EQUAL TO CONTINUE ALPHABETIC LOWERCASE """
        password = "abcdefgh"
        str1 = string.ascii_lowercase
        if password in str1:
            print("Most common password")

    def test_check_password_alphabetic_uppercase_pattern(self):
        """ TEST FOR PASSWORD NOT CONTINUE OF ALPHABETIC UPPERCASE """
        password = "ABCDEFGH"
        str1 = string.ascii_uppercase
        if password in str1:
            print("Most common used password")

    def test_check_user_is_active(self):
        """ TEST FOR USER IS ACTIVE OR NOT """
        user = User.objects.get(pk=1)
        if user.is_active:
            print("User is active")
        else:
            print("User is not active")

    def test_check_user_exists(self):
        """ TEST FOR USER IS EXISTS OR NOT """
        user = User.objects.filter(id=3).count()
        if user:
            print("User Exists")
        else:
            print("User not exists")

    def test_check_user_login(self):
        user = User.objects.create(username="govinda")
        user.set_password(12345678)
        user.save()
        c = Client()
        logged_in = c.login(username="govinda", password=12345678)
        if logged_in:
            print("Logged in successfully!")
        else:
            print("Invalid Credentials!")

class UserProfileTest(TestCase):
    """BASIC TESTS"""
    def setup(self):
        super(UserProfileTest, self).setup()

    def test_valid_birth_date(self):
        print("check valid birth date")