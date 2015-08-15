from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import * 


def hello(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def index(request):
    return HttpResponse("Hello, world. You're at the microfinance index.")

def getGurukulByCity(request, city_id):
    GurukulList = get_object_or_404(gurukul, city_id = city_id)
    return HttpResponse("The city asked for was %s." % city_id)

def getStudentByGurukul(request, gurukul_id):
    StudentList = get_object_or_404(student, st_gk_id = gurukul_id)
    return HttpResponse("The gurukul_id was %s." % gurukul_id)

def getStudentInfo(request, student_id):
    StudentProfile = get_object_or_404(student, id = student_id)
    return HttpResponse("The student_id was %s." % student_id)

def getSponsorInfo(request, sponsor_id):
    SponsorProfile = get_object_or_404(sponsor, id = sponsor_id)
    return HttpResponse("The student_id was %s." % student_id)
