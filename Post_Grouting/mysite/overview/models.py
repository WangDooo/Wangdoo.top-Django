from django.db import models
from django.contrib.auth.models import User

class Totalpile(models.Model):
	name = models.CharField(max_length=20, unique=True)
	number = models.IntegerField()

	class Meta:
		ordering = ("id",)

	def __str__(self):
		return self.name

class Originalpile(models.Model):
	name = models.CharField(max_length=20, unique=True)

	class Meta:
		ordering = ("id",)

	def __str__(self):
		return self.name

class Trypile(models.Model):
	name = models.CharField(max_length=20, unique=True)

	class Meta:
		ordering = ("id",)

	def __str__(self):
		return self.name