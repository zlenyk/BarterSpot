from django.db import models
from django.contrib.auth.models import User, UserManager
from BarterSpot.announcements.models import Announcement


class BarterUser(User):
    objects = UserManager()

    city = models.CharField(max_length=100)

    @staticmethod
    def createUser(username,
                   first_name,
                   last_name,
                   email,
                   password,
                   city,
                   validate=True):
        newUser = BarterUser.objects.create_user(username=username,
                                                 email=email,
                                                 first_name=first_name,
                                                 last_name=last_name,
                                                 password=password,
                                                 city=city,
                                                 )
        if validate:
            newUser.is_active = False

        newUser.save()
        return newUser

    @staticmethod
    def userWithLoginExists(login):
        if BarterUser.objects.filter(username=login):
            return True
        else:
            return False

    @staticmethod
    def userWithIdExists(id):
        if BarterUser.objects.filter(id=id):
            return True
        else:
            return False

    @staticmethod
    def getUserByLogin(login):
        if BarterUser.userWithLoginExists(login):
            return BarterUser.objects.get(username=login)
        else:
            return None

    @staticmethod
    def getUserById(id):
        if BarterUser.userWithIdExists(id):
            return BarterUser.objects.get(id=id)
        else:
            return None

    @staticmethod
    def getUserFromRequest(request):
        return BarterUser.getUserById(request.user.id)

    @staticmethod
    def getUserByFirstName(_first_name):
        return BarterUser.objects.filter(first_name=_first_name)

    @staticmethod
    def getUserByLastName(_last_name):
        return BarterUser.objects.filter(last_name=_last_name)

    @staticmethod
    def getUserByNames(_first_name, _last_name):
        return BarterUser.objects.filter(first_name=_first_name,
                                         last_name=_last_name)

    def getLogin(self):
        return self.get_username()

    def getCity(self):
        return self.city

    def getAnnouncements(self, orderBy='pub_date'):
        return Announcement.getUsersAnnouncements(self, orderBy)

    def updateUserData(self, _first_name, _last_name, _email, _city):
	self.first_name = _first_name
	self.last_name =_last_name
	self.email =_email
	self.city = _city
	self.save()

    def validate(self):
        self.is_active = True
        self.save()


class Validation(models.Model):
    user = models.ForeignKey("BarterUser")
    code = models.CharField(max_length=40)

    @staticmethod
    def createValidation(user, strHash):
        newVal = Validation(user=user, code=strHash)
        newVal.save()
        return newVal

    @staticmethod
    def validate(validation):
        validation.user.validate()
        validation.delete()
        # Validation.objects.delete(validation)

    @staticmethod
    def validationExists(strHash):
        return Validation.objects.filter(code=strHash).count() != 0

    @staticmethod
    def getValidation(strHash):
        if Validation.validationExists(strHash):
            return Validation.objects.get(code=strHash)
        else:
            return None
