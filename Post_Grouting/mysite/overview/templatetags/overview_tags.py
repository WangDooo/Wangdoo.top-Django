from django import template

register = template.Library()

from overview.models import Totalpile, Originalpile, Trypile
from grout.models import Grout

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