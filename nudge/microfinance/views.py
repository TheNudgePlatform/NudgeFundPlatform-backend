from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

def hello(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
