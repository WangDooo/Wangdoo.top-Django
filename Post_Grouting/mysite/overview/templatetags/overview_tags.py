from django import template

register = template.Library()

from overview.models import Totalpile, Originalpile, Trypile
from grout.models import Grout

import datetime

@register.simple_tag
def total_pile():
	sum_pile = 0
	pile = Totalpile.objects.all()
	for each in pile:
		sum_pile = sum_pile + each.number
	return sum_pile

@register.simple_tag
def original_pile():
	return Originalpile.objects.count()

@register.simple_tag
def try_pile():
	return Trypile.objects.count()

@register.simple_tag
def grout_amount():
	return Grout.objects.count()

@register.simple_tag
def total_grout_amount():
	sum_amount = 0
	grout = Grout.objects.all()
	for each in grout:
		sum_amount = sum_amount + each.amount
	return round(sum_amount,3)

@register.simple_tag
def today_pile_amount():
	today =  datetime.datetime.now().strftime("%Y-%m-%d")
	today_pile_amount = Grout.objects.filter(grout_date=today).count()
	return today_pile_amount

@register.simple_tag
def today_grout_amount():
	amount = 0
	today =  datetime.datetime.now().strftime("%Y-%m-%d")
	grout_today = Grout.objects.filter(grout_date=today)
	for each in grout_today:
		amount = amount + each.amount
	return round(amount,3)