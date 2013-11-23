from django.db import models

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

