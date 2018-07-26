from django.contrib import admin
from .models import Kaisai

class KaisaiAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'created', 'image')
	list_filter = ("user",)

admin.site.register(Kaisai, KaisaiAdmin)