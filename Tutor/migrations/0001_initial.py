# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=b'D', max_length=2, choices=[(b'J', b'Junior college'), (b'P', b'Polytechnic'), (b'U', b'University'), (b'D', b'Not Specified')])),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Graduation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Date of graduation')),
                ('description', models.CharField(max_length=500)),
                ('education', models.ForeignKey(to='Tutor.Education')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=b'D', max_length=2, choices=[(b'P', b'Primary School'), (b'O', b'O-level'), (b'A', b'A-level'), (b'D', b'Not Specified')])),
                ('title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(default=b'D', max_length=2, choices=[(b'E', b'East'), (b'W', b'West'), (b'C', b'Central'), (b'N', b'North'), (b'D', b'Unknown')])),
                ('time', models.CharField(default=b'D', max_length=2, choices=[(b'M', b'Morning'), (b'A', b'Afternoon'), (b'E', b'Evening'), (b'D', b'Not Specified')])),
                ('gender', models.CharField(default=b'D', max_length=2, choices=[(b'F', b'Female'), (b'M', b'Male'), (b'D', b'Not Specified')])),
                ('name', models.CharField(max_length=100)),
                ('education', models.ManyToManyField(to='Tutor.Education', through='Tutor.Graduation')),
                ('subject_teach', models.ManyToManyField(to='Tutor.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='graduation',
            name='tutor',
            field=models.ForeignKey(to='Tutor.Tutor'),
            preserve_default=True,
        ),
    ]
