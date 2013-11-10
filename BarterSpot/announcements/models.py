from django.db import models
from BarterSpot.users.models import Member
from datetime import datetime


class Tag(models.Model):
    name = models.CharField(max_length=100)
    # count = models.AutoField(primaty_key=True)

    def __unicode__(self):
        return self.name

    @staticmethod
    def tagExists(strTagName):
        return Tag.objects.filter(name=strTagName).count() != 0

    @staticmethod
    def addTag(strTagName):
        if not Tag.tagExists(strTagName):
            Tag(name=strTagName).save()
        return Tag.objects.get(name=strTagName)

    @staticmethod
    def addTagsList(tagsStrList):
        ret = []
        for tag in tagsStrList:
            ret.append(Tag.addTag(tag))

        return ret


class Announcement(models.Model):
    member = models.ForeignKey(Member)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField('date of announcement',
                                    default=datetime.today())

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
        return self.title

    def addTagsList(self, tagsList):
        for tag in tagsList:
            self.tags.add(tag)
