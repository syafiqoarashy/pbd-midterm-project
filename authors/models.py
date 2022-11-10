from django.db import models
from submission.models import Submission

# Create your models here.
class Authors(models.Model):
    submission_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.CharField(max_length=30)
    organization = models.CharField(max_length=100)
    web_page = models.URLField()
    person_id = models.IntegerField()
    correspon = models.BooleanField(null=True)
    full_name = models.TextField()