from django.db import models


# Create your models here.

class Member(models.Model):
	username = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)

