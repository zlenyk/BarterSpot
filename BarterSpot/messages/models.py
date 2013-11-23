from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):

    OFFER = 0
    SYSTEM = 1
    ORDINARY = 2 # a user-to-user message different from an offer

    TYPE = (
        (OFFER, 'offer'),
        (SYSTEM, 'system'),
        (ORDINARY, 'ordinary'),
    )

    m_type = models.CharField(choices=TYPE, max_length=10)
    sender = models.ForeignKey('users.BarterUser', related_name='message_senders')
    recipient = models.ForeignKey('users.BarterUser', related_name='message_recipients')
    subject = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.today())

    @staticmethod
    def sendMessage(_m_type, _sender, _recipient, _subject, _body):
        msg = Message(
            m_type = _m_type,
            sender = _sender,
            recipient = _recipient,
            subject = _subject,
            body = _body,
        )
        msg.save()
        return msg

    @staticmethod
    def getMessagesTo(_recipient):
        try:
            return Message.objects.filter(recipient=_recipient)
        except Message.DoesNotExist:
            return None
    
    @staticmethod
    def getMessagesFrom(_sender):
        try:
            return Message.objects.filter(sender=_sender)
        except Message.DoesNotExist:
            return None
    
