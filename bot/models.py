from email import message
from django.db import models

# Create your models here.


class Message(models.Model):
    message = models.CharField(max_length=20, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True, default=0)
    minutes = models.IntegerField(null=True, blank=True, default=0)
    seconds = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
