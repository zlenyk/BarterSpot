from django.db import models
# import BarterSpot.users.models
from datetime import datetime


class Tag(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    @staticmethod
    def getTagByName(self, strTagName):
        if Tag.tagExists(strTagName):
            return self.objects.get(name=strTagName)
        return None

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

    def incrementCount(self):
        self.count += 1
        self.save()

    def decrementCount(self):
        self.count -= 1
        self.save()

    def getCount(self):
        return self.count

    @staticmethod
    def getTagsByPopularity():
        pass


class Announcement(models.Model):
    user = models.ForeignKey("users.BarterUser")
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

    @staticmethod
    def createAnnouncement(user, title, content, tagsList):
        newAnn = Announcement(
            user=user,
            title=title,
            content=content,
        )
        newAnn.save()
        newAnn.addTagsList(tagsList)
        return newAnn

    @staticmethod
    def getAllAnnouncements(orderBy='pub_date'):
        return Announcement.objects.order_by(orderBy)

    @staticmethod
    def getUsersAnnouncements(user, orderBy='pub_date'):
        return Announcement.objects.filter(user=user).order_by(orderBy)

    def __unicode__(self):
        return self.title

    def getAuthor(self):
        return self.user

    def getAuthorLogin(self):
        return self.getAuthor().getLogin()

    def getTitle(self):
        return self.title

    def getContent(self):
        return self.content

    def addTag(self, tag):
        tag.incrementCount()
        self.tags.add(tag)

    def addTagsList(self, tagsList):
        for tag in tagsList:
            self.addTag(tag)

    def addStrTag(self, strTag):
        self.addTag(Tag.addTag(strTag))

    def addStrTagsList(self, strTagsList):
        for strTag in strTagsList:
            self.addStrTag(strTag)

    def removeTag(self, tag):
        tag.decrementCount()
        self.tags.remove(tag)

    def removeTagsList(self, tagsList):
        for tag in tagsList:
            self.removeTag(tag)

    def removeStrTag(self, strTag):
        tagToRemove = Tag.getTagByName(strTag)
        if tagToRemove is not None:
            self.removeTag(tagToRemove)

    def getSimilarAnnouncements():
        pass
