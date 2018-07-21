from django.db import models
from django.contrib.auth.models import User

from slugify import slugify


def upload_kaisai_path(instance, filename):
    filename = instance.name+'.jpg' #图片名称
    return "images_kaisai/{file}".format(file=filename)    #保存路径和格式

class Kaisai(models.Model):
	user = models.ForeignKey(User, related_name="kaisai", on_delete=models.CASCADE) 
	name = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(max_length=500, blank=True)
	created = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to=upload_kaisai_path)

	class Meta:
		ordering = ("name",)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Kaisai, self).save(*args, **kwargs)
