#EasyAceSite/views
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import  RequestContext, loader

def getHome(request):
    template = loader.get_template('index.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getTestimonial(request):
    template = loader.get_template('testimonial.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getWelfare(request):
    template = loader.get_template('welfare.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getAbout(request):
    template = loader.get_template('about.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getContact(request):
    template = loader.get_template('contact.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getFAQ(request):
    template = loader.get_template('faq.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))