from django import template
from myshopping.models import *
from django.db.models import Sum

register = template.Library()

# @register.inclusion_tag('myshopping/_our_basket_total.html')
@register.assignment_tag
def basket_total():
    list_cats = Cart.objects.all().aggregate(basket=Sum('price'))
    return list_cats['basket']