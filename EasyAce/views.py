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

#the following is for Chinese version of site
def getHome(request):
    template = loader.get_template('index_zh.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getTestimonialZH(request):
    template = loader.get_template('testimonial_zh.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getWelfareZH(request):
    template = loader.get_template('welfare_zh.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getAboutZH(request):
    template = loader.get_template('about_zh.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getContactZH(request):
    template = loader.get_template('contact_zh.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def getFAQZH(request):
    template = loader.get_template('faq_zh.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))