# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0004_auto_20151010_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='time',
        ),
        migrations.AddField(
            model_name='tutor',
            name='type',
            field=models.CharField(default=b'P', max_length=2, choices=[(b'F', b'Full-Time'), (b'P', b'Part-Time')]),
        ),
    ]
