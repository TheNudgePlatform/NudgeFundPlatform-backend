from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import SponsorWallet
from .models import Sponsor
from .models import SponsorTransactionHistory
from .models import SponsorFundHistory
import datetime
def hello(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def sponsor(request, sponsor_id):
    template = loader.get_template('sponsor.html')
    context = {}
    context['GetWalletBalance'] = getWalletBalance(sponsor_id)
    context['loan_make_payment'] = loan_make_payment(sponsor_id, 1L, 100, 12345464)
    return render(request, 'sponsor.html', context)

def getInvestmentHistory(request, sponsor_id):
   template = loader.get_template('profile.html')
   ihistory = sponsorFundHistory.objects.get(sponsor_id=sponsor_id)
   context = {}
   context['investmentHistory'] = ihistory
   return render(request, 'profile.html', context)

def loan_make_payment(sponsor_id, student_id, amount, transactionHistoryId):
    if requiredFundsAvailable(sponsor_id, amount):
      debitWallet(sponsor_id, amount)
      updateSponsorFundHistory(sponsor_id, transactionHistoryId, student_id, 
      amount, True)
      return True
    else:
      #prompt add to wallet
      return False

def getWalletBalance(sponsor_id):
    obj = SponsorWallet.objects.get(sp_id=sponsor_id)
    return obj.fund

def getSponsorInfo(sponsor_id):
    return Sponsor.objects.get(id=sponsor_id)

def requiredFundsAvailable(sponsor_id, amount):
    walletBalance = getWalletBalance(sponsor_id)
    return walletBalance >= amount

def creditWallet(sponsor_id, amount):
    obj = SponsorWallet.objects.get(sp_id=sponsor_id)
    #call payment gateway
    #transactionReferenceId is returned by payment gateway
    transactionReferenceId = qwertyBFJrnfveuyfdbewjkf;
    # amount has to be positive
    obj.fund = obj.fund + amount
    obj.save()
    thistoryId = updateTransactionHistory(sponsor_id, transactionRefId, False, amount)
    return thistoryId

def debitWallet(sponsor_id, amount):
    #throw error if amount > walletBalance
    obj = SponsorWallet.objects.get(sp_id=sponsor_id)
    obj.fund -= amount
    obj.save()
    transactionRefId = 'jfbekjfwmnkjdbklekfjbkhrfv';
    thistoryId = updateTransactionHistory(sponsor_id, transactionRefId, True, amount)
    return thistoryId

def updateTransactionHistory(sponsor_id, transactionRefId, isDebit, amount):
    SponsorTransactionHistory.objects.create(sponsor_id=sponsor_id, txn_amt=amount, 
    txn_ref=transactionRefId, txn_date=datetime.datetime.now(), txn_is_debit=isDebit) 

def updateSponsorFund(sponsor_id, amount):
   obj = SponsorWallet.objects.get(sponsor_id=sponsor_id)
   obj.fund = amount
   obj.save()

def updateSponsorFundHistory(sponsorId, transactionId, studentId, amount, 
   isDebit):
   SponsorFundHistory.objects.create(sponsor_id=sponsorId, student_id=studentId,
   txn_hist_id=transactionId, amount=amount, txn_create_id=datetime.datetime.now(), 
   txn_is_debit= isDebit)      
