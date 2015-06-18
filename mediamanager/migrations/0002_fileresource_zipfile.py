# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileresource',
            name='zipfile',
            field=models.FileField(upload_to=b'zipfilesofattachedfiles/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
