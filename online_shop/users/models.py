from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.IntegerField(null=True, blank=True)
	adress = models.TextField(default='my adress')

	def __str__(self):
		return str(self.user.username)