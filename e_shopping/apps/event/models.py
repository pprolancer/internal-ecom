from django.db import models
from sorl.thumbnail import ImageField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime, date
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

    @property
    def is_past_due(self):
        dt_tz = self.event_start_datetime
        dt = dt_tz.replace(tzinfo=None)
        current_datetime = datetime.today()
        dtt = current_datetime.replace(microsecond=0)
        if dtt > dt:
            return False
        return False


class EventGiftCondition(models.Model):
    from_user = models.ForeignKey(UserProfile,
        related_name="from_userevent", blank=True, null=True)
    to_user = models.ForeignKey(UserProfile,
        related_name="to_userevent", blank=True, null=True)
    event = models.ForeignKey(Event,related_name="event",blank=True,null=True)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
            verbose_name = "EventGift"
            verbose_name_plural = "EventGifts"

    def add(self,from_user,student_events):
        try:
            for student_event in student_events:
                student_event_id = student_event.split(",")
                student = UserProfile.objects.get(id=student_event_id[1])
                event = Event.objects.get(id=student_event_id[0])

                event, created = EventGiftCondition.objects.get_or_create(from_user=from_user,
                    to_user=student,event=event,item_price=student_event_id[2],product_count=1)
                event.save()
        except:
            pass
        return True
