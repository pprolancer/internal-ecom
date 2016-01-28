from django.shortcuts import render
from myshopping.models import *
from django.views.generic import View, TemplateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
import json

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
        product = Product.objects.get(id=get_id)
        ctx = {'product':product,'categories':categories}
        return render(request, "myshopping/product_detail.html", ctx)

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('add_basket',None)
        products = Product.objects.filter(id=product_id)
        all_cart = Cart.objects.all()
        cart_add = Cart() 
        quantity = "1"
        cart =  Cart.objects.filter(product_id=product_id,user_id=request.user)
        if not cart:
            cart_add.add(request.user,products[0],products[0].product_price,quantity)
        ctx = {'products':all_cart}
        return render(request, "myshopping/addtobasket.html", ctx)

class RemoveFromCartView(View):

    """ Remove Product from Cart """
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id',None)
        cart_id = request.POST.get('cart_id',None)
        cart = Cart.objects.get(pk=cart_id,product_id=product_id,user_id=request.user)
        cart.delete()
        return HttpResponse(
            json.dumps({'status': True,'cart_id':cart_id}), content_type="application/json")


class UpdateCartView(View):

    """ Remove Product from Cart """
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('save_later',None)
        quantity= request.POST.get('quantity',None)
        # total_price = request.POST.get('total_price',None)
        cart = Cart.objects.get(product_id=product_id,user_id=request.user)
        if cart:
            cart = Cart.objects.filter(product_id=product_id,user_id=request.user).update(quantity=quantity)

        return HttpResponse(
            json.dumps({'status': True,'product_id':product_id}), content_type="application/json")