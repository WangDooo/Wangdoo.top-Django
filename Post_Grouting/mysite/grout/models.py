from django.db import models
from django.contrib.auth.models import User

from slugify import slugify
import django.utils.timezone as timezone
import datetime

class Grout(models.Model):
	user = models.ForeignKey(User, related_name="grout", on_delete=models.CASCADE) 
	name = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(max_length=500, blank=True)
	grout_date = models.DateField(default=timezone.now)
	amount = models.FloatField()
	remark = models.CharField(max_length=500, blank=True)

	class Meta:
		ordering = ("id",)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Grout, self).save(*args, **kwargs)

class Report(models.Model):
	user = models.ForeignKey(User, related_name="report", on_delete=models.CASCADE)
	report = models.CharField(max_length=500, blank=True)
	date = models.DateField(default=timezone.now)

	class Meta:
		ordering = ("-date",)

class Surplus(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE) 
	amount_today = models.FloatField(default=0)
	amount_sum = models.FloatField(default=0)
	conversion_number = models.IntegerField(default=0)
	reward = models.IntegerField(default=0)
	date = models.DateField(default=timezone.now)
	remaining = models.FloatField(default=0)

	class Meta:
		ordering = ("id",)

class Remaining(models.Model):
	user = models.ForeignKey(User, related_name="remaining", on_delete=models.CASCADE)
	remain = models.FloatField(default=0)
	date = models.DateField(default=timezone.now)

