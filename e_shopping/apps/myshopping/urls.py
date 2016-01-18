from django.conf.urls import  url
from django.views.generic import TemplateView
from myshopping.views import *

urlpatterns = [

    url(r'^home$', HomeView.as_view(), name="home")
   
]