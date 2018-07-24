from django import template

register = template.Library()

from overview.models import Totalpile, Originalpile, Trypile

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