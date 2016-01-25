from django.shortcuts import render
from myshopping.models import *
from django.views.generic import View, TemplateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
from carton.cart import Cart
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



class AddToBasketView(View):

    """ Show Product into Basket """


    def get(self, request, *args, **kwargs):
        get_id = kwargs['pk']
        products = Product.objects.filter(id=get_id)
        ctx = {'products':products}
        return render(request, "myshopping/addtobasket.html", ctx)