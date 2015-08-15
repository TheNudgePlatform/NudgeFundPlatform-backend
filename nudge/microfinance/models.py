import datetime
from django.db import models
from django.utils import timezone

class sponsor(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateTimeField()

class sponsor_fund(models.Model):
    fund = models.IntegerField(default=0)

class city(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    modified_on = models.DateField(default=timezone.now)

class skill_sets(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    modified_on = models.DateField(default=timezone.now)

class language(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    modified_on = models.DateField(default=timezone.now)

class gurukul(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    modified_on = models.DateField(default=timezone.now)

class gurukul_batch(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    gurukul_id = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    language_id = models.IntegerField(default=0)
    skillset_ids = models.CharField(max_length=1000)
    gender = models.CharField(max_length=1)
    student_ids = models.CharField(max_length=1000)
    modified_on = models.DateField(default=timezone.now)

class student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    profile_image = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=1)
    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=500,null=True)
    email_id = models.CharField(max_length=100,null=True)
    phone_no = models.CharField(max_length=14,null=True)
    postal_address = models.CharField(max_length=500,null=True)
    enrolment_date = models.DateField(max_length=500)
    modified_on = models.DateField(default=timezone.now)
