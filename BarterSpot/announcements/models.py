from django.db import models
from BarterSpot.users.models import Member
from datetime import datetime
# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=100)
	count = models.IntegerField(default=0)
        def __unicode__(self):
	    return self.name;

class Announcement(models.Model):
	member = models.ForeignKey(Member)
	title = models.CharField(max_length=100)
	content = models.TextField()
	tags = models.ManyToManyField(Tag)
	pub_date = models.DateTimeField('date of announcement',default=datetime.today())
	

	ACTIVE = 0
	IN_PROGRESS = 1
	FINISHED = 2
        STATUS = (
	    (ACTIVE, 'active'),
	    (IN_PROGRESS, 'in_progress'),
	    (FINISHED, 'finished'),
	)

        status = models.IntegerField(choices=STATUS, default=ACTIVE)

        def __unicode__(self):
	    return self.title;



