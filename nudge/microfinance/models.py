from django.db import models

class sponsor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    profile_image = models.CharField(max_length=400)
    gender = models.CharField(max_length=5)
    description = models.CharField(max_length=500)
    email_id = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=14, default='00919999999999')
    postal_address = models.CharField(max_length=500)
    modified_on = models.DateField(default=timezone.now)
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.name)

class sp_wallet(models.Model):
    wallet_id = models.AutoField(promary_key=True, unique=True)
    id = models.IntegerField()
    fund = models.IntegerField(default=0)
    wallet_mod = models.DateField(default=timezone.now)

class sp_txn(models.Model):
    txn_id = models.AutoField(primary_key=True, unique=True)
    id = models.IntegerField()
    txn_amt = models.IntegerField()
    txn_ref = models.CharField(max_length=50)
    txn_date = models.DateField(default=timezone.now)
    txn_is_debit = models.BooleanField()
    
class sp_txn_hst(models.Model):
    txn_hist_id = models.AutoField(promary_key=True, unique=True)
    id = models.IntegerField()
    txn_id = models.IntegerField()
    st_id = models.IntegerField()
    amnt = models.IntegerField()
    txn_create_id = models.DateField()
    txn_is_debit_hst = models.BooleanField()

    
