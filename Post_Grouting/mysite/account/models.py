from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE) 
	realname = models.CharField(max_length=20)
	invitation_code = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)

	def __str__(self):
		return 'user {}'.format(self.user.username)

