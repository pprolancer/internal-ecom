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
        products = Product.objects.filter(id=get_id)
        ctx = {'products':products,'categories':categories}
        return render(request, "myshopping/product_detail.html", ctx)


class ShoppingCartView(View):
    def post(self, request, *args, **kwargs):
        get_id = request.POST['data']
        c_user = request.user
        current_user = c_user.pk
        # user = User.objects.get(username = current_user)
        chk_productcount = ShoppingCart.objects.filter(user_id=user)
        # return HttpResponse(
        #     json.dumps({'status': endors}), content_type="application/json")
# employeeendorsementsview = EmployeeEndorsementsView.as_view()        



class AddToCartView(View):

    """ Show Product into Cart """
    def get(self, request, *args, **kwargs):
        get_id = kwargs['pk']
        all_cart = Cart.objects.all()
        products = Product.objects.filter(id=get_id)
        cart = Cart()
        quantity = "1"
        if request.user.is_authenticated():
            cart.add(request.user,products[0],products[0].product_price,quantity)
        ctx = {'products':all_cart}
        return render(request, "myshopping/addtobasket.html", ctx)


class RemoveFromCartView(View):

    """ Remove Product from Cart """
    def post(self, request, *args, **kwargs):
        get_id = request.POST.get('data',None)
        cart = Cart.objects.get(id=get_id,user_id=request.user)
        cart.delete()
        return HttpResponse(
            json.dumps({'status': True,'get_id':get_id}), content_type="application/json")


class UpdateCartView(View):

    """ Remove Product from Cart """
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('remove_cart_id',None)
        quantity= request.POST.get('quantity',None)
        cart = Cart.objects.filter(pk=get_id,user_id=request.user).update(quantity=quantity )
        return HttpResponse(
            json.dumps({'status': True,'get_id':get_id}), content_type="application/json")