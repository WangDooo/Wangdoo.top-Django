from django.contrib import admin
from .models import Grout, Report, Surplus, Remaining

class GroutAdmin(admin.ModelAdmin):
	list_display = ('name', 'amount', 'grout_date', 'remark', 'user')
	list_filter = ("user",)

admin.site.register(Grout, GroutAdmin)

class ReportAdmin(admin.ModelAdmin):
	list_display = ('report', 'date', 'user')
	list_filter = ("user",)

admin.site.register(Report, ReportAdmin)

class SurplusAdmin(admin.ModelAdmin):
	list_display = ('user', 'amount_today', 'amount_sum', 'conversion_number', 'reward', 'date', 'remaining')
	list_filter = ("user",)

admin.site.register(Surplus, SurplusAdmin)

class RemainingAdmin(admin.ModelAdmin):
	list_display = ('remain', 'date', 'user')
	list_filter = ("date",)

admin.site.register(Remaining, RemainingAdmin)