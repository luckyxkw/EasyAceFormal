#Tutor/urls
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getTutor, name='tutor'),
    url(r'^(?P<subject_title>[a-z|A-Z]+)/$', views.getTutorBySubject, name='tutor_subject'),
]
