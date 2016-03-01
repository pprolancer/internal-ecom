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


    def test_check_unique_username(self):
        """ TEST unique username """
        user = User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
        if User.objects.filter(username='john').count():
            print("username already exists")

