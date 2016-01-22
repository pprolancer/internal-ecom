from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Relationship(models.Model):
    from_person = models.ForeignKey(User, related_name='from_people')
    to_person = models.ForeignKey(User, related_name='to_people')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Relationship"
        verbose_name_plural = "Relationships"

