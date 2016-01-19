from django.shortcuts import render
from myshopping.models import *
from django.views.generic import View, TemplateView, CreateView

# Create your views here.
class HomeView(View):

    """ Show Product with Category """

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()
        ctx = {'categories':categories,'products':products}
        return render(request, "myshopping/home.html", ctx)



class Product_detailView(View):

    """ Show Product with Category """

    def get(self, request, *args, **kwargs):
        get_id = kwargs['pk']
        categories = Category.objects.all()
        products = Product.objects.filter(id=get_id)
        ctx = {'products':products,'categories':categories}
        return render(request, "myshopping/product_detail.html", ctx)