from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import  RequestContext, loader
from .models import Tutor, Subject

def getTutor(request):
    template = loader.get_template('Tutors.html')
    tutor = Tutor.objects.all()
    context = RequestContext(request, {
            'tutors':tutor,
    })
    return HttpResponse(template.render(context))

def getTutorBySubject(request, subject_title):
    template = loader.get_template('Tutors.html')
    try:
        subject = Subject.objects.get(title=subject_title)
        tutor = Tutor.objects.filter(subject_teach=subject)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    context = RequestContext(request, {
            'tutors':tutor,
    })
    #name = ', '.join([p.name for p in tutor])
    return HttpResponse(template.render(context))