from django.db import models
import datetime
from django.utils import timezone

class CustomUser(models.Model):
    brand = models.CharField('', max_length=100,  db_index=True)
    model = models.CharField('', max_length=100,  db_index=True)
    your_name = models.CharField('',max_length=50, blank=False)
    email = models.CharField('', max_length=50, db_index=True)
    date_posted= models.DateTimeField((''), default=timezone.now)
