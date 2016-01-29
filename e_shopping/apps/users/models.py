from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='profile')
    user_role = models.CharField("User Role",max_length=100, db_index=True)
    product_count = models.IntegerField(default=0)
    product_price_limit = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

class Relationship(models.Model):
    from_person = models.ForeignKey(User, related_name='from_people')
    to_person = models.ForeignKey(User, related_name='to_people')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Relationship"
        verbose_name_plural = "Relationships"


