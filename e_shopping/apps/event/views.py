from django.shortcuts import render
from event.models import (Event)
from users.models import UserProfile
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class EventView(View):

    """ Show User Event """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, "event/event.html", {})
