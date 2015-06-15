# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanage', '0002_auto_20150519_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachedfiles',
            name='thumbnail',
            field=models.ImageField(upload_to=b'thumbnails/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
