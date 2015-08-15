import datetime
from django.db import models
from django.utils import timezone

class sponsor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    profile_image = models.ImageField(height_field=100, width_field=100,null=True)
    gender = models.CharField(max_length=1)
    description = models.CharField(max_length=500,default='')
    email_id = models.EmailField(max_length=100,null=True)
    phone_no = models.CharField(max_length=14, default='00919999999999')
    postal_address = models.CharField(max_length=500,null=True)
    modified_on = models.DateField(default=timezone.now)
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.name)

class sp_wallet(models.Model):
    sp_id = models.IntegerField(unique=True)
    fund = models.IntegerField(default=0)
    modified_on = models.DateField(default=timezone.now)

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
    profile_image = models.ImageField(height_field=100, width_field=100,null=True)
    gender = models.CharField(max_length=1)
    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=500,null=True)
    email_id = models.EmailField(max_length=100,null=True)
    phone_no = models.CharField(max_length=14,null=True)
    postal_address = models.CharField(max_length=500,null=True)
    enrolment_date = models.DateField(max_length=500)
    modified_on = models.DateField(default=timezone.now)

class sp_txn(models.Model):
    txn_id = models.AutoField(primary_key=True, unique=True)
    id = models.IntegerField(default=0)
    txn_amt = models.IntegerField(default=0)
    txn_ref = models.CharField(max_length=50)
    txn_date = models.DateField()
    txn_is_debit = models.BooleanField()
    
class sp_txn_hst(models.Model):
    txn_hist_id = models.AutoField(primary_key=True, unique=True)
    id = models.IntegerField(default=0)
    txn_id = models.IntegerField(default=0)
    st_id = models.IntegerField(default=0)
    amnt = models.IntegerField(default=0)
    txn_create_id = models.DateField()
    txn_is_debit_hst = models.BooleanField()
