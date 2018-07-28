from django import forms

from .models import Grout, Report

class GroutForm(forms.ModelForm):
	class Meta:
		model = Grout
		fields = ('name', 'amount','grout_date', 'remark')

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ('report', 'date')