from django import template
from myshopping.models import (Category, Product, Cart, ProductImage, Order)
from django.db.models import Sum
from users.models import Relationship, UserProfile
from event.models import Event, EventGiftCondition

register = template.Library()

@register.assignment_tag
def basket_total(products):
    gt= 0.0
    for product in products:
        gt += quantity_price_total(product)
    return gt

@register.assignment_tag
def quantity_price_total(product):
    try:
        total = float(product.product.product_price) *  int(product.quantity) 
    except:
        total = 0.0
    return  total


@register.inclusion_tag('myshopping/_myshopping_category.html')
def catergory_lists():
    catergory_lists = Category.objects.all()
    return {'catergory_lists': catergory_lists }


@register.assignment_tag
def parent_student_name(from_user):
    relationships = from_user.profile.from_people.all()
    childs = []
    for relationship in relationships:
        childs.append(relationship)
    return childs


@register.assignment_tag
def student_event(student_id):
    events = Event.objects.filter(user_id=student_id)
    return events


@register.assignment_tag
def student_event_price_itemcount(student_id):
    student_counts = UserProfile.objects.filter(id=student_id)
    return student_counts


@register.assignment_tag
def current_user_event_count(parent_id,student_id,event_id):
    parentid = UserProfile.objects.get(user_id=parent_id)
    event_count = EventGiftCondition.objects.filter(from_user_id=parentid,
            to_user_id=student_id,event_id=event_id).count()
    if event_count:
        user_profile_gift_count = UserProfile.objects.get(id=student_id).product_count
        user_event_count =  user_profile_gift_count - event_count
        if user_event_count <=0:
            current_user_event_count = 0
        else:
            current_user_event_count = user_event_count

    else:
        current_user_event_count = UserProfile.objects.get(id=student_id).product_count
    return current_user_event_count


@register.assignment_tag
def current_user_event_pricelimit(parent_id,student_id,event_id):

    parentid = UserProfile.objects.get(user_id=parent_id)

    
    pricelimit = EventGiftCondition.objects.filter(from_user_id=parentid.id,
        to_user_id=student_id,event_id=event_id).aggregate(Sum('item_price'))
    try:
        total_price = int(pricelimit['item_price__sum'])
        studentlimit = UserProfile.objects.get(id=student_id)
        user_event_pricelimit = studentlimit.product_price_limit - total_price

        if user_event_pricelimit<=0:
            current_user_event_pricelimit = 0
        else:
            current_user_event_pricelimit = user_event_pricelimit
    except:
        current_user_event_pricelimit = UserProfile.objects.get(id=student_id).product_price_limit
        
    return current_user_event_pricelimit


@register.assignment_tag
def current_user_count(parent_id):
    current_user_count = UserProfile.objects.get(user_id=parent_id)
    return current_user_count
