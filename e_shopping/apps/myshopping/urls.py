from django.conf.urls import  url
from django.views.generic import TemplateView
from myshopping.views import *

urlpatterns = [

    url(r'^home/$', HomeView.as_view(), name="home"),
    url(r'^productdetail/(?P<pk>\d+)/$', Product_detailView.as_view(), name="product_detail"),
    url(r'^remove_frpm_cart/$', RemoveFromCartView.as_view(), name="remove_frpm_cart"),
    url(r'^update_product/$', UpdateCartView.as_view(), name="update_product"),
    url(r'^processd_to_checkout/$', ProcessdCheckout.as_view(), name="processd_to_checkout"),
    url(r'^myshopping-checkout/$', CheckoutList.as_view(), name="myshopping-checkout"),
    url(r'^addtobasket/$', AddToCartView.as_view(), name="add_to_basket"),
    url(r'^sendemail/$', SendMailToAdmin.as_view(), name="sendmail_to_admin"),
]