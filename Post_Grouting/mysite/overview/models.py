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

class Piledetail(models.Model):
	name = models.CharField(max_length=20, unique=True)
	pile_length = models.IntegerField()
	pile_diameter = models.FloatField()
	pipe_layer_d = models.IntegerField()
	pipe_layer_c = models.IntegerField()
	soil_d = models.CharField(max_length=50)
	grout_amount_d = models.FloatField()
	grout_amount_c = models.FloatField()
	grout_amount = models.FloatField()

	class Meta:
		ordering = ("id",)

	def __str__(self):
		return self.name