# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0003_auto_20150929_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduation',
            name='date',
        ),
        migrations.AlterField(
            model_name='graduation',
            name='description',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
