from django.db import models
from django.db.models import Q
from datetime import datetime

# Create your models here.

class Transaction(models.Model):

    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2
    
    STATUS = (
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected'),
    )

    source_user = models.ForeignKey('users.BarterUser', related_name='transactions_source_users');
    target_user = models.ForeignKey('users.BarterUser', related_name='transactions_target_users');
    status = models.CharField(choices=STATUS, max_length=10)
    source_ann = models.ForeignKey('announcements.Announcement', related_name='transactions_source_anns')
    target_ann = models.ForeignKey('announcements.Announcement', related_name='transactions_target_anns')
    offer_date = models.DateTimeField(default=datetime.today())
    response_date = models.DateTimeField(null=True, default=None)

    def getStatus(self):
        return self.STATUS[int(self.status)][1]

    @staticmethod
    def createTransaction(_source_user, _target_user, _status, _source_ann, _target_ann):
        tr = Transaction(
            source_user = _source_user,
            target_user = _target_user,
            status = _status,
            source_ann = _source_ann,
            target_ann = _target_ann,
        )
        tr.save()

    @staticmethod
    def getTransactionById(tid):
        try:
            return Transaction.objects.get(pk=tid)
        except Transaction.DoesNotExist:
            return None

    @staticmethod
    def getFinishedTransactionsFrom(user):
        try:
            return Transaction.objects.filter(
                Q(source_user=user), Q(status=Transaction.ACCEPTED) | Q(status=Transaction.REJECTED) )
        except Transaction.DoesNotExist:
            return None

    @staticmethod
    def getFinishedTransactionsTo(user):
        try:
            return Transaction.objects.filter(
                Q(target_user=user), Q(status=Transaction.ACCEPTED) | Q(status=Transaction.REJECTED) )
        except Transaction.DoesNotExist:
            return None

    @staticmethod
    def getPendingTransactionsFrom(user):
        try:
            return Transaction.objects.filter(source_user=user, status=Transaction.PENDING)
        except Transaction.DoesNotExist:
            return None

    @staticmethod
    def getPendingTransactionsTo(user):
        try:
            return Transaction.objects.filter(target_user=user, status=Transaction.PENDING)
        except Transaction.DoesNotExist:
            return None
            

    @staticmethod
    def getAllTransactionsFromAndTo(user):
        try:
            return Transaction.objects.filter(Q(target_user=user) | Q(source_user=user))
        except Transaction.DoesNotExist:
            return None

    @staticmethod
    def getAllTransactionsTo(target_id):
        try:
            return Transaction.objects.filter(target_user=target_id)
        except Transaction.DoesNotExist:
            return None

    @staticmethod
    def getAllTransactionFrom(source_id):
        try:
            return Transaction.objects.filter(source_user=source_id)
        except Transaction.DoesNotExist:
            return None

    
