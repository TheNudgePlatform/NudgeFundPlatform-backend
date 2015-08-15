from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import sp_wallet
from .models import sponsor
from .models import sponsor_transaction_history
from .models import sponsor_fund_history

def hello(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def getWalletBalance(sponsor_id):
    obj = sponsor_wallet.get(sp_id=sponsor_id)
    return obj.fund

def getSponsorInfo(sponsor_id):
    return sponsor.get(id=sponsor_id)

def requiredFundsAvailable(sponsor_id, amount):
    walletBalance = getWalletBalance(request, sponsor_id)
    return walletBalance >= amount

def creditWallet(sponsor_id, amount):
    obj = sponsor_wallet.get(sp_id=sponsor_id)
    #call payment gateway
    #transactionReferenceId is returned by payment gateway
    transactionReferenceId = qwertyBFJrnfveuyfdbewjkf;
    # amount has to be positive
    obj.fund = obj.fund + amount
    return transactionReferenceId

def debitWallet(sponsor_id, amount):
    #throw error if amount > walletBalance
    obj.fund = sponsor_wallet.get(sp_id=sponsor_id)
    obj.fund -= amount
    transactionReferenceId = qwertyBFJrnfveuyfdbewjkf;
    return transactionReferenceId

def updateTransactionHistory(sponsor_id, transactionRefId, isDebit, amount):
    sponsor_transaction_history.create(sponsor_id=sponsor_id, txn_amt=amount, txn_ref=transactionRefId, txn_date=now(), txn_is_debit=isDebit) 

def updateSponsorFund(sponsor_id, amount)
   obj = sponsor_wallet.get(sponsor_id)
   obj.fund = amount

def updateSponsorFundHistory(sponsorId, transactionId, studentId, amount, isDebit):
   sponsor_fund_history.create(sponsor_id=sponsorId, student_id=studentId, txn_hist_id=transactionId, amount=amount, modified_on=now(), txn_is_debit= isDebit)isDebit)       
