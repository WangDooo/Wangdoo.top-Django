from django import forms
from slugify import slugify

from .models import Kaisai

class KaisaiForm(forms.ModelForm):
	class Meta:
		model = Kaisai
		fields = ('name', 'image')

