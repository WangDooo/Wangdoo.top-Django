from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'realname', 'phone')
	list_filter = ("phone",)

admin.site.register(UserProfile, UserProfileAdmin)