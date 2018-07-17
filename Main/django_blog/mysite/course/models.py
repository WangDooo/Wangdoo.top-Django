from django.db import models
from django.contrib.auth.models import User

from slugify import slugify
from .fields import OrderField

class Course(models.Model):
	user = models.ForeignKey(User, related_name='courses_user', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	overview = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	student = models.ManyToManyField(User, related_name="courses_joined", blank=True)

	class Meta:
		ordering = ('-created',)

	def save(self, *args, **kargs):
		self.slug = slugify(self.title)
		super(Course, self).save(*args, **kargs)

	def __str__(self):
		return self.title

def user_directory_path(instance, filename):
	return "course/user_{0}/{1}".format(instance.user.id, filename)

class Lesson(models.Model):
	user = models.ForeignKey(User, related_name="lesson_user", on_delete=models.CASCADE)
	course = models.ForeignKey(Course, related_name="lesson", on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	# video = models.FileField(upload_to="videos")
	video = models.FileField(upload_to=user_directory_path)
	description = models.TextField(blank=True)
	# attach = models.FileField(upload_to="attachs", blank=True)
	attach = models.FileField(upload_to=user_directory_path, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	order = OrderField(blank=True, for_fields=['course'])

	class Meta:
		ordering = ['order']

	def __str__(self):
		return '{}.{}'.format(self.order, self.title)