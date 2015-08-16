import datetime
from django.db import models
from django.utils import timezone

class Sponsor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    profile_image = models.ImageField(upload_to='/static/',null=True)
    gender = models.CharField(max_length=1, default='M')
    description = models.CharField(max_length=500,default='')
    email_id = models.EmailField(max_length=100,blank=True)
    phone_no = models.CharField(max_length=14,blank=True)
    postal_address = models.CharField(max_length=500,blank=True)
    modified_on = models.DateField(default=timezone.now)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.name)

class SponsorWallet(models.Model):
    sp_id = models.IntegerField(unique=True)
    fund = models.IntegerField(default=0)
    modified_on = models.DateField(default=timezone.now)

class City(models.Model):

    def __unicode__(self):
        return u'%s' % self.name

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    modified_on = models.DateField(default=timezone.now)

class SkillSets(models.Model):

    def __unicode__(self):
        return u'%s' % self.name

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    modified_on = models.DateField(default=timezone.now)

class Language(models.Model):

    def __unicode__(self):
        return u'%s' % self.name

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    modified_on = models.DateField(default=timezone.now)

class Gurukul(models.Model):

    def __unicode__(self):
        return u'%s' % self.name

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    city_id = models.IntegerField(default=0)
    modified_on = models.DateField(default=timezone.now)

class GurukulBatch(models.Model):
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

class Student(models.Model):

    def __unicode__(self):
        return u"%s" % self.name

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    profile_image = models.ImageField(upload_to='/static/', null=True)
    gender = models.CharField(max_length=1)
    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=500,blank=True)
    email_id = models.EmailField(max_length=100,blank=True)
    phone_no = models.CharField(max_length=14,blank=True)
    postal_address = models.CharField(max_length=500,blank=True)
    enrolment_date = models.DateField(max_length=500)
    gurukul_id = models.IntegerField()
    modified_on = models.DateField(default=timezone.now)

class SponsorTransactionHistory(models.Model):
    txn_id = models.AutoField(primary_key=True, unique=True)
    sponsor_id = models.IntegerField(default=0)
    txn_amt = models.IntegerField(default=0)
    txn_ref = models.CharField(max_length=50)
    txn_date = models.DateField()
    txn_is_debit = models.BooleanField()

class SponsorFundHistory(models.Model):
    txn_hist_id = models.IntegerField(default=0)
    sponsor_id = models.IntegerField(default=0)
    student_id = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    txn_create_id = models.DateField()
    txn_is_debit = models.BooleanField()
