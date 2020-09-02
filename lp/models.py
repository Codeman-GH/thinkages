from django.db import models
from django.db import models
from django.utils import timezone
from thinkages import settings
from django import forms
import datetime
from time import time

# Create your models here.


class LeaveReply(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date_posted = models.DateTimeField('Date Posted')


    class Meta:
        verbose_name_plural = "Replies"

    
    
