from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import SponsorWallet
from .models import Sponsor
from .models import SponsorTransactionHistory
from .models import SponsorFundHistory, Student
from .models import *

import datetime

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def studentListing(request):
    template = loader.get_template('list.html')
    students = Student.objects.all()
    cities = City.objects.all()
    gurukuls = Gurukul.objects.all()
    context = RequestContext(request,{'student_list':students,'city_list':cities,'gurukul_list':gurukuls})
    return HttpResponse(template.render(context))

def studentListingGurukul(request,g_id):
    template = loader.get_template('list.html')
    students = Student.objects.all().filter(gurukul_id=g_id)
    cities = City.objects.all()
    gurukuls = Gurukul.objects.all()
    context = RequestContext(request,{'student_list':students,'city_list':cities,'gurukul_list':gurukuls})
    return HttpResponse(template.render(context))

def studentListingCity(request,c_id):
    template = loader.get_template('list.html')
    cities = City.objects.all()
    gurukuls = Gurukul.objects.all()
    gurukuls_city = Gurukul.objects.all().filter(city_id=c_id)
    gurukul_ids = []
    for g in gurukuls_city:
        gurukul_ids.append(g.id)
    students = Student.objects.all().filter(gurukul_id__in=gurukul_ids)
    context = RequestContext(request,{'student_list':students,'city_list':cities,'gurukul_list':gurukuls})
    return HttpResponse(template.render(context))

def studentListingGender(request,gender_type):
    template = loader.get_template('list.html')
    students = Student.objects.all().filter(gender=gender_type)
    cities = City.objects.all()
    gurukuls = Gurukul.objects.all()
    context = RequestContext(request,{'student_list':students,'city_list':cities,'gurukul_list':gurukuls})
    return HttpResponse(template.render(context))

def student(request, student_id):
    template = loader.get_template('student-detail.html')

    student = get_object_or_404(Student, id=student_id)

    ctx = {
            'student': student
            }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))

def sponsorInfo(request, sponsor_id):
    template = loader.get_template('profile.html')
    sponsor = Sponsor.objects.get(sponsor_id)
    context['sponsor'] = sponsor
    return render(request, 'profile.html', context)

def sponsor(request, sponsor_id):
    template = loader.get_template('sponsor.html')
    context = {}
    context['GetWalletBalance'] = getWalletBalance(sponsor_id)
    context['loan_make_payment'] = loan_make_payment(sponsor_id, 1L, 100, 12345464)
    return render(request, 'sponsor.html', context)

def investmentHistory(request, sponsor_id):
   template = loader.get_template('profile.html')
   ihistory = []
   ihistory = SponsorFundHistory.objects.filter(sponsor_id=sponsor_id)
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

def students(request):
    template = loader.get_template('index.html')
    students = Student.objects.all()
    context = RequestContext(request,{'students_list':students})
    return HttpResponse(template.render(context))

def students_city(request, city_id):
    template = loader.get_template('index.html')

def students_gurukul(request, gurukul_id):
    student_list = []
    template = loader.get_template('index.html')
    students = student.objects.all().filter(language=language_id)
    for s in students:
        student_list.append({'name':s.name})
    context = RequestContext(request,{'students_list':student_list})
    return HttpResponse(template.render(context))

def students_language(request, language_id):
    student_list = []
    template = loader.get_template('index.html')
    students = student.objects.all().filter(language=language_id)
    for s in students:
        student_list.append({'name':s.name})
    context = RequestContext(request,{'students_list':student_list})
    return HttpResponse(template.render(context))

def students_gender(request, req_gender):
    template = loader.get_template('index.html')
    student_list = []
    template = loader.get_template('index.html')
    students = student.objects.all().filter(gender=req_gender)
    for s in students:
        student_list.append({'name':s.name})
    context = RequestContext(request,{'students_list':student_list})
    return HttpResponse(template.render(context))

def updateSponsorFundHistory(sponsorId, transactionId, studentId, amount,
   isDebit):
   SponsorFundHistory.objects.create(sponsor_id=sponsorId, student_id=studentId,
   txn_hist_id=transactionId, amount=amount, txn_create_id=datetime.datetime.now(),
   txn_is_debit= isDebit)
