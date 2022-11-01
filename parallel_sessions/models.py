from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Tracks(models.Model):
    symposium = models.CharField(max_length = 20)
    title = models.TextField()

class Sessions(models.Model):
#     id_paper = models.CharField(max_length = 20)
#     room = models.CharField(max_length = 15)
#     session = models.IntegerField()
#     date = models.DateField()
#     time = models.TextField()
#     location = models.CharField(max_length = 20)
#     author = models.TextField()
#     paper = models.TextField()
    symposium_T = models.ForeignKey(Tracks, on_delete=models.CASCADE)

class SessionsSCE(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsIT(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsSBCC(models.Model):
    id_paper = models.CharField(max_length = 20)
    room =models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsECE(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsCPE(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsBBE(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsMME(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsAME(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsIE(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()

class SessionsISBE(models.Model):
    id_paper = models.CharField(max_length = 20)
    room = models.CharField(max_length = 15)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TextField()
    location = models.CharField(max_length = 20)
    author = models.TextField()
    paper = models.TextField()
