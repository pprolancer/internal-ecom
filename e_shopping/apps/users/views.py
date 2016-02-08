import re
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from users.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        ctx = {"form": form}
        return render(request, "registration/register.html", ctx)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        password = request.POST.get('password')
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            messages.success(
                request,
                'User registered successfully, Now wait for admin approval.')
            return HttpResponseRedirect(self.get_success_url())
        ctx = {"form": form}
        return render(request, "registration/register.html", ctx)

    def get_success_url(self):
        url = reverse('home')
        return url


class LoginView(View):


    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        ctx = {"form": form}
        return render(request, "registration/login.html", ctx)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return HttpResponseRedirect(self.get_success_url())
        ctx = {"form": form}
        return render(request, "registration/login.html", ctx)

    def get_success_url(self):
        url = reverse('welcome')
        return url


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        url = reverse('user-login')
        return url


class IndexView(View):

    """ Show Product with Category """

    def get(self, request, *args, **kwargs):

        return render(request, "index.html", {})

