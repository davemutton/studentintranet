# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachedfiles',
            name='icon',
            field=models.CharField(max_length=254, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachedfiles',
            name='attachedfile',
            field=models.FileField(upload_to=b'attachedfiles/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
