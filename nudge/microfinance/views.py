from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import sp_wallet
from .models import sponsor
def hello(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def getWalletBalance(request, sponsor_id):
    wallet_balance = sp_wallet.get(sp_id=sponsor_id)
    return wallet_balance

def getSponsorInfo(request, sponsor_id):
    return sponsor.get(id=sponsor_id)

def requiredFundsAvailable(request, sponsor_id, amount):
    walletBalance = getWalletBalance(request, sponsor_id)
    return walletBalance >= amount

define creditWallet(request, sponsor_id, amount):
    walletBalance = sp_wallet.get(sp_id=sponsor_id)
    #call payment gateway
    #transactionReferenceId is returned by payment gateway
    transactionReferenceId = qwertyBFJrnfveuyfdbewjkf;
    # amount has to be positive
    sp_wallet.put(sp_id=sponsor_id, walletBalance + amount)
    return transactionReferenceId

define debitWallet(request, sponsor_id, amount):
    #throw error if amount > walletBalance
    walletBalance = sp_wallet.get(sp_id=sponsor_id)
    sp_wallet.put(sp_id=sponsor_id, walletBalance - amount)
    transactionReferenceId = qwertyBFJrnfveuyfdbewjkf;
    updateTransactionHistory(sponsor_id, amount, "credit", transactionReferenceId)

define updateSponsorFund(request, sponsor_id, amount)
   sp_wallet.put(sp_id=sponsor_id, amount)

define updateSponsorFundHistory(sponsorId, transactionId, studentId, amount):
     
