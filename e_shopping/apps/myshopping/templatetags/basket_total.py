from django import template
from myshopping.models import (Category, Product, Cart, ProductImage, Order)
from django.db.models import Sum
from users.models import Relationship, UserProfile
from event.models import Event

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
    student_counts = UserProfile.objects.filter(id=student_id)
    return events


@register.assignment_tag
def student_event_price_itemcount(student_id):
    student_counts = UserProfile.objects.filter(id=student_id)
    return student_counts
