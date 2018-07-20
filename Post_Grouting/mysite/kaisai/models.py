from django.db import models
from django.contrib.auth.models import User

from slugify import slugify

class Kaisai(models.Model):
	user = models.ForeignKey(User, related_name="kaisai", on_delete=models.CASCADE) 
	name = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(max_length=500, blank=True)
	created = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to='images_kaisai')

	class Meta:
		ordering = ("name",)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Kaisai, self).save(*args, **kwargs)