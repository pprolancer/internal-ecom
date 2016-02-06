from django.conf.urls import  url
from django.views.generic import TemplateView
from event.views import (EventView)

urlpatterns = [

    url(r'^event/$', EventView.as_view(), name="event"),
    
    ]