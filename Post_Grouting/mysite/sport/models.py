from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

class Punchcard(models.Model):
	user = models.ForeignKey(User, related_name="sport", on_delete=models.CASCADE) 
	sport = models.CharField(max_length=50, blank=True)
	remark = models.CharField(max_length=500, blank=True)
	publish_time = models.DateTimeField(default=timezone.now)
	publish_date = models.DateField(default=timezone.now)

	class Meta:
		ordering = ("-publish_time",)
