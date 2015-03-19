# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlResource',
            fields=[
                ('defaultresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mediamanager.DefaultResource')),
                ('url', models.URLField(max_length=400)),
            ],
            options={
            },
            bases=('mediamanager.defaultresource',),
        ),
    ]
