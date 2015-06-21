# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0002_fileresource_zipfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileresource',
            name='files',
            field=models.ManyToManyField(related_name='files', to='filemanage.AttachedFiles', blank=True),
            preserve_default=True,
        ),
    ]
