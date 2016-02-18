from django.shortcuts import render
from myshopping.models import (Category, Product, Cart, ProductImage, Order)
from django.views.generic import View, TemplateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
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
from event.models import Event,EventGiftCondition
# Create your views here.


class IndexView(View):

    """ Show Student for whom Parent have to buy gift """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        # request.user.profile.get_child()
        return render(request, "index.html", {})

    def post(self, request, *args, **kwargs):
        return redirect(reverse('home'))



class HomeView(View):

    """ Show Product with Category """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()
        ctx = {'categories':categories,'products':products}
        return render(request, "myshopping/home.html", ctx)

class ProductDetailView(View):

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
        try:
            product_id = request.POST.get('add_basket','')
            to_user = request.POST.getlist('to_person_id','')
            student_event_ids = request.POST.getlist('student_event_id','')
            insert_student_event = EventGiftCondition()
            insert_student_event.add(request.user.profile,student_event_ids)
            products = Product.objects.filter(id=product_id)
            event_id = []
            student_id = []

            for student_event in student_event_ids:
                student_event_id = student_event.split(",")
                event_id.append(student_event_id[0])
                student_id.append(student_event_id[1])

            all_cart = Cart.objects.filter(from_user=request.user.profile,
                to_user_id__in=student_id,event_id__in=event_id)

            cart_add = Cart() 
            quantity = "1"

            cart =  Cart.objects.filter(product_id=product_id,
                from_user=request.user.profile,to_user_id__in=student_id,event_id__in=event_id)
            if not cart:
                cart_add.add(request.user.profile,student_event_ids
                    ,products[0],products[0].product_price,
                    quantity)

            ctx = {'products':all_cart}

            return redirect(reverse('add_to_basket'))
        except KeyError:
            return redirect(reverse('user-login'))

class RemoveFromCartView(View):

    """ Remove Product from Cart """

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            product_id = request.POST.get('product_id','')
            cart_id = request.POST.get('cart_id','')
            to_user = request.POST.get('to_user','')
            cart = Cart.objects.filter(pk=cart_id,product_id=product_id,
                from_user=request.user.profile,to_user_id=to_user)
            cart.delete()
            return HttpResponse(
                json.dumps({'status': True,'cart_id':cart_id}), content_type="application/json")
        except KeyError:
            return redirect(reverse('user-login'))

class UpdateCartView(View):

    """ Update Product Quantity Of Cart """
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        product_id = request.POST.get('save_later','')
        quantity= request.POST.get('quantity','')
        to_user = request.POST.get('to_user','')
        to_user_profile = UserProfile.objects.filter(id=to_user)
        
        cart = Cart.objects.get(product_id=product_id,
               from_user=request.user.profile,to_user=to_user_profile)
        if cart:
            cart = Cart.objects.filter(product_id=product_id,
                   from_user=request.user.profile,to_user=to_user_profile).update(quantity=quantity)

        return HttpResponse(
            json.dumps({'status': True,'product_id':product_id}), 
            content_type="application/json")


class ProcessdCheckout(View):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        
        studentevent_ids = request.POST.getlist('studentevent_id[]','')
        student_ids = []
        event_ids = []
        for studentevent_id in studentevent_ids:
            event_ids.append(studentevent_id[0])
            student_ids.append(studentevent_id[2])
        
        for studentevent_id in studentevent_ids:

            current_login_user = UserProfile.objects.get(user_id=request.user)
            if (current_login_user.product_count!=0) or (current_login_user.product_price_limit!=0):
                student_current_count = EventGiftCondition.objects.filter(from_user=request.user.profile,
                to_user_id=studentevent_id[2],event_id=studentevent_id[0])

                student_count_userprofile = UserProfile.objects.get(id=studentevent_id[2])
                if student_current_count.count() <= student_count_userprofile.product_count:

                    cart_remove = Cart.objects.filter(from_user=request.user.profile,
                        to_user_id=studentevent_id[2],event_id=studentevent_id[0])
                    for i in cart_remove:
                        order , created = Order.objects.get_or_create(from_user=request.user.profile,
                            to_user_id=studentevent_id[2],event_id=studentevent_id[0],
                            product_id=i.product_id,item_quantity=i.quantity,
                            item_price=i.price,order_status='Pending')
                        order.save()

                        cart_delete = Cart.objects.filter(from_user=request.user.profile,
                        to_user_id=studentevent_id[2],event_id=studentevent_id[0],product_id=i.product_id)
                        cart_delete.delete()
                else:
                    return HttpResponse(
                        json.dumps({'status': 'student_limit_exceed'}), content_type="application/json")

            else:
                return HttpResponse(
                    json.dumps({'status': 'exceed'}), content_type="application/json")
                

        return HttpResponse(
                    json.dumps({'status': True}), content_type="application/json")                               


class CheckoutList(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request,'myshopping/checkout.html',{})


class AddToCartView(View):

    """ Show Product into Basket """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user_id=request.user)
        all_cart = Cart.objects.filter(from_user_id=user_profile)
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
        import pdb;pdb.set_trace()
        user_profile = UserProfile.objects.get(user_id=request.user)
        orders = Order.objects.filter(user_id=user_profile)
        subject = "Cinnemohills Online shopping"
        data_dict = {'orders':orders}
        message = render_to_string(
                    "email/notification.html", data_dict)

        from_email = 'info@cinnamonhills.com'
        to_user = 'store@vdavis.me'
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, [to_user])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse(
                json.dumps({'status': 'send_mail'}), content_type="application/json")
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
