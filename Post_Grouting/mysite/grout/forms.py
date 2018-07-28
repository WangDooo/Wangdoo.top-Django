from django import forms

from .models import Grout

class GroutForm(forms.ModelForm):
	class Meta:
		model = Grout
		fields = ('name', 'amount','grout_date', 'remark')

