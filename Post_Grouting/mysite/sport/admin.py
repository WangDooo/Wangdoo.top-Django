from django.contrib import admin
from .models import Punchcard

class SportAdmin(admin.ModelAdmin):
	list_display = ('user', 'sport', 'remark', 'publish_time')
	list_filter = ("user",)

admin.site.register(Punchcard, SportAdmin)
# Register your models here.
