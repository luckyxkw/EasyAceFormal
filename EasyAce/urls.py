#EasyAceSite/urls
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from . import views

urlpatterns = patterns('',
    url(r'^$', 'EasyAce.views.getHome', name='home'),
    url(r'^testimonial/$', 'EasyAce.views.getTestimonial', name='testimonial'),
    url(r'^welfare/$', 'EasyAce.views.getWelfare', name='welfare'),
    url(r'^aboutus/$', 'EasyAce.views.getAbout', name='about'),
    url(r'^contact/$', 'EasyAce.views.getContact', name='contact'),
    url(r'^faq/$', 'EasyAce.views.getFAQ', name='faq'),
    url(r'^zhhome/$', 'EasyAce.views.getHomeZH', name='homeZH'),
    url(r'^zh/testimonial/$', 'EasyAce.views.getTestimonialZH', name='testimonialZH'),
    url(r'^zh/welfare/$', 'EasyAce.views.getWelfareZH', name='welfareZH'),
    url(r'^zh/aboutus/$', 'EasyAce.views.getAboutZH', name='aboutZH'),
    url(r'^zh/contact/$', 'EasyAce.views.getContactZH', name='contactZH'),
    url(r'^zh/faq/$', 'EasyAce.views.getFAQZH', name='faqZH'),
	url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)

