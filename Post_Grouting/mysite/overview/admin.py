from django.contrib import admin
from .models import Trypile, Totalpile, Originalpile

class TrypileAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Trypile, TrypileAdmin)

class TotalpileAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'number')

admin.site.register(Totalpile, TotalpileAdmin)

class OriginalpileAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Originalpile, OriginalpileAdmin)