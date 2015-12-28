from django.contrib import admin
from .models import Tutor, Subject, Education, Graduation

class GraduationInline(admin.TabularInline):
    model = Graduation
    extra = 1

class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')

admin.site.register(Tutor, TutorAdmin)
admin.site.register(Subject)
admin.site.register(Education)
admin.site.register(Graduation)
