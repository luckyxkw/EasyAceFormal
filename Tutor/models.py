from django.db import models
from django.conf import settings
# Create your models here.
class Subject(models.Model):
    LEVEL = (
        ('P', 'Primary School'),
        ('O', 'O-level'),
        ('A', 'A-level'),
        ('D', 'Not Specified'),
    )
    level = models.CharField(max_length=2, choices=LEVEL, default='D')
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Education(models.Model):
    LEVEL = (
        ('J', 'Junior college'),
        ('P', 'Polytechnic'),
        ('U', 'University'),
        ('D', 'Not Specified'),
    )
    level = models.CharField(max_length=2, choices=LEVEL, default='D')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tutor(models.Model):
    REGION = (
        ('E', 'East'),
        ('W', 'West'),
        ('C', 'Central'),
        ('N', 'North'),
        ('D', 'Unknown'),
    )
    TIME = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening'),
        ('D', 'Not Specified'),
    )
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('D', 'Not Specified'),
    )
    TYPE = (
        ('F', 'Full-Time'),
        ('P', 'Part-Time'),
    )
    region = models.CharField(max_length=2, choices=REGION, default='D')
    gender = models.CharField(max_length=2, choices=GENDER, default='D')
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="tutor")
    subject_teach = models.ManyToManyField(Subject)
    education = models.ManyToManyField(Education,through='Graduation')
    type = models.CharField(max_length=2, choices=TYPE, default='P')
              
    def __str__(self):
        return self.name


class Graduation(models.Model):
    tutor = models.ForeignKey(Tutor)
    education = models.ForeignKey(Education)
    #date = models.DateTimeField('Date of graduation', blank = True)
    description = models.CharField(max_length=500, blank = True)
