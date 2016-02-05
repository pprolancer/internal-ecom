from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.
USER_TYPES = (
    ('parent', 'PARENT'),
    ('student', 'STUDENT'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile')
    user_role = models.CharField(
        "User Role", max_length=50, choices=USER_TYPES)
    product_count = models.IntegerField(default=0)
    product_price_limit = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0)])
    

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return '{0} - {1}'.format(self.user.username, self.user_role)



class Relationship(models.Model):
    from_person = models.ForeignKey(UserProfile, related_name='from_people')
    to_person = models.ForeignKey(UserProfile, related_name='to_people')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Relationship"
        verbose_name_plural = "Relationships"



