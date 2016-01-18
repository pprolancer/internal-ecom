from django.shortcuts import render
from myshopping.models import *
from django.views.generic import View, TemplateView, CreateView

# Create your views here.
class HomeView(View):

    """ Show Product with Category """

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        ctx = {'categories':categories}
        return render(request, "myshopping/home.html", ctx)
