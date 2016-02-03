from django.shortcuts import render
from myshopping.models import *
from django.views.generic import View, TemplateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
from users.models import UserProfile
from django.shortcuts import render_to_response
from django.db.models import Sum
from django.contrib import messages
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.conf import settings
# Create your views here.


class HomeView(View):

    """ Show Product with Category """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()
        ctx = {'categories':categories,'products':products}
        return render(request, "myshopping/home.html", ctx)

class Product_detailView(View):

    """ Show Product Detail Page """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        get_id = kwargs['pk']
        categories = Category.objects.all()
        product = Product.objects.get(id=get_id)
        ctx = {'product':product,'categories':categories}
        return render(request, "myshopping/product_detail.html", ctx)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('add_basket',None)
        products = Product.objects.filter(id=product_id)
        all_cart = Cart.objects.filter(user_id=request.user)
        cart_add = Cart() 
        quantity = "1"
        cart =  Cart.objects.filter(product_id=product_id,user_id=request.user)
        if not cart:
            cart_add.add(request.user,products[0],products[0].product_price,quantity)
        ctx = {'products':all_cart}
        return redirect(reverse('add_to_basket'))



class RemoveFromCartView(View):

    """ Remove Product from Cart """

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id',None)
        cart_id = request.POST.get('cart_id',None)
        cart = Cart.objects.get(pk=cart_id,product_id=product_id,user_id=request.user)
        cart.delete()
        return HttpResponse(
            json.dumps({'status': True,'cart_id':cart_id}), content_type="application/json")


class UpdateCartView(View):

    """ Update Product Quantity Of Cart """
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('save_later',None)
        quantity= request.POST.get('quantity',None)
        cart = Cart.objects.get(product_id=product_id,user_id=request.user)
        if cart:
            cart = Cart.objects.filter(product_id=product_id,user_id=request.user).update(quantity=quantity)

        return HttpResponse(
            json.dumps({'status': True,'product_id':product_id}), content_type="application/json")

class ProcessdCheckout(View):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        user_quantity = Cart.objects.filter(user_id=request.user).aggregate(total=Sum('quantity'))
        user_price = Cart.objects.filter(user_id=request.user).aggregate(total=Sum('price'))
        profile_user = UserProfile.objects.get(user_id=request.user)
        if (user_quantity['total'] <= profile_user.product_count) and (user_price['total']<= profile_user.product_price_limit):
            cart_remove = Cart.objects.filter(user_id=request.user)
            for i in cart_remove:
                order , created = Order.objects.get_or_create(user=request.user,
                    product_id=i.product_id,item_quantity=i.quantity,item_price=i.price,order_status='Pending')
                order.save()
                cart_delete = Cart.objects.filter(user=request.user,product_id=i.product_id)
                cart_delete.delete()

            return HttpResponse(
                    json.dumps({'status': 'true'}), content_type="application/json")
        else:
            return HttpResponse(
        json.dumps({'status': 'uptoresult'}), content_type="application/json")


class CheckoutList(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,'myshopping/checkout.html',{})


class AddToCartView(View):

    """ Show Product into Basket """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        all_cart = Cart.objects.filter(user_id=request.user)
        try:
            profile_user = UserProfile.objects.get(user_id=request.user)
            ctx = {'products':all_cart}
            return render(request, "myshopping/addtobasket.html", ctx)
        except:
            messages.warning(request,
                'Admin does not grant permission for shopping')
            return render(request, "myshopping/addtobasket.html", {'status':'False'})


class SendMailToAdmin(View):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        subject = "Cinnemohills Online shopping"
        data_dict = {'orders':orders}
        message = render_to_string(
                    "email/notification.html", data_dict)

        from_email = settings.EMAIL_HOST_USER
        to_user = 'info@cinnamonhills.com'
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, [to_user])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse(
                json.dumps({'status': 'send_mail'}), content_type="application/json")
            # return HttpResponseRedirect('/contact/thanks/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
