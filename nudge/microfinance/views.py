from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import SponsorWallet
from .models import Sponsor
from .models import SponsorTransactionHistory
from .models import SponsorFundHistory

def hello(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def getWalletBalance(sponsor_id):
    obj = SponsorWallet.get(sp_id=sponsor_id)
    return obj.fund

def getSponsorInfo(sponsor_id):
    return Sponsor.get(id=sponsor_id)

def requiredFundsAvailable(sponsor_id, amount):
    walletBalance = getWalletBalance(request, sponsor_id)
    return walletBalance >= amount

def creditWallet(sponsor_id, amount):
    obj = SponsorWallet.get(sp_id=sponsor_id)
    #call payment gateway
    #transactionReferenceId is returned by payment gateway
    transactionReferenceId = qwertyBFJrnfveuyfdbewjkf;
    # amount has to be positive
    obj.fund = obj.fund + amount
    return transactionReferenceId

def debitWallet(sponsor_id, amount):
    #throw error if amount > walletBalance
    obj.fund = SponsorWallet.get(sp_id=sponsor_id)
    obj.fund -= amount
    transactionReferenceId = qwertyBFJrnfveuyfdbewjkf;
    return transactionReferenceId

def updateTransactionHistory(sponsor_id, transactionRefId, isDebit, amount):
    SponsorTransactionHistory.create(sponsor_id=sponsor_id, txn_amt=amount, txn_ref=transactionRefId, txn_date=now(), txn_is_debit=isDebit) 

def updateSponsorFund(sponsor_id, amount)
   obj = SponsorWallet.get(sponsor_id=sponsor_id)
   obj.fund = amount

def updateSponsorFundHistory(sponsorId, transactionId, studentId, amount, isDebit):
   SponsorFundHistory.create(sponsor_id=sponsorId, student_id=studentId, txn_hist_id=transactionId, amount=amount, modified_on=now(), txn_is_debit= isDebit)isDebit)       
