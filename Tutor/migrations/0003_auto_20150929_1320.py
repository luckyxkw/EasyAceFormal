# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0002_tutor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='photo',
            field=models.ImageField(upload_to=b'tutor'),
            preserve_default=True,
        ),
    ]
