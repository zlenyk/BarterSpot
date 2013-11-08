from django.db import models


# Create your models here.

class Member(models.Model):
	username = models.CharField(max_length=100)
	city = models.CharField(max_length=100)

