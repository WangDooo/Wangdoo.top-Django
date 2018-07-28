from django.contrib import admin
from .models import Grout, Report

class GroutAdmin(admin.ModelAdmin):
	list_display = ('name', 'amount', 'grout_date', 'remark', 'user')
	list_filter = ("user",)

admin.site.register(Grout, GroutAdmin)

class ReportAdmin(admin.ModelAdmin):
	list_display = ('report', 'date', 'user')
	list_filter = ("user",)

admin.site.register(Report, ReportAdmin)