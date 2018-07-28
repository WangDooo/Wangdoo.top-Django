from django.db import models
from django.contrib.auth.models import User

from slugify import slugify
from django.utils import timezone

class Grout(models.Model):
	user = models.ForeignKey(User, related_name="grout", on_delete=models.CASCADE) 
	name = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(max_length=500, blank=True)
	grout_date = models.DateField(default=timezone.now())
	amount = models.FloatField()
	remark = models.TextField(max_length=500, blank=True)

	class Meta:
		ordering = ("id",)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Grout, self).save(*args, **kwargs)