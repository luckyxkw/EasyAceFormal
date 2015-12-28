# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='photo',
            field=models.CharField(default=b'unknown.png', max_length=100),
            preserve_default=True,
        ),
    ]
