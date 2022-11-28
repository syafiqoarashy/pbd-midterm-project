from dataclasses import Field
from distutils.command.upload import upload
from django.db import models

class Speakers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=75)
    country = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    profile = models.TextField()
    storagePath = models.CharField(max_length=100)
    speechTitle = models.CharField(max_length=100, null=True)
    speechAbstract = models.TextField()
    time = models.DateTimeField()
    room = models.CharField(max_length=20)
    symposium = models.CharField(max_length=100)