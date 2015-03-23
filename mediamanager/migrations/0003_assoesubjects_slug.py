# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0002_urlresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='assoesubjects',
            name='slug',
            field=models.SlugField(max_length=100, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
