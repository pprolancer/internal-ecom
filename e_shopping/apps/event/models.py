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
EVENT_TYPE = (

('PersonalEvent','PERSONALEVENT'),
('Holiday','HOLIDAY'),
    )

class Event(models.Model):
    user = models.ForeignKey(UserProfile ,
    related_name="user_event", blank=True, null=True)
    event_type = models.CharField(
        max_length=128,
        choices=EVENT_TYPE,
        default=EVENT_TYPE[0][0]
    )
    event_title = models.CharField("Event Title", max_length=255, blank=True, null=True)
    event_start_datetime = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(
        "Event Comment", max_length=255, blank=True, null=True)
    created_date = models.DateField(
        auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventGiftCondition(models.Model):
    from_user = models.ForeignKey(UserProfile,
        related_name="from_userevent", blank=True, null=True)
    to_user = models.ForeignKey(UserProfile,
        related_name="to_userevent", blank=True, null=True)
    event = models.ForeignKey(Event,related_name="event",blank=True,null=True)

    class Meta:
            verbose_name = "EventGift"
            verbose_name_plural = "EventGifts"

    def add(self,from_user,to_users,event):
        try:
            for to_user in to_users:
                cart, created = Cart.objects.get_or_create(from_user=from_user,
                    product=product,price=price, quantity= quantity,to_user=to_user)
                cart.save()
        except:
            pass
        return True
    