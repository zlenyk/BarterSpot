from django.db import models
from BarterSpot.users.models import Member

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=100)
	count = models.IntegerField(default=0)

class Announcement(models.Model):
	member = models.ForeignKey(Member)
	title = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)
	pub_date = models.DateTimeField('date of announcement')




