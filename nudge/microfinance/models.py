from django.db import models

class sponsor(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateTimeField()

class sponsor_fund(models.Model):
    fund = models.IntegerField(default=0)
