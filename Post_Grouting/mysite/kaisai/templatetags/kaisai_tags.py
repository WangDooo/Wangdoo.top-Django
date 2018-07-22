from django import template

register = template.Library()

from kaisai.models import Kaisai

@register.simple_tag
def total_kaisai():
	return Kaisai.objects.count()