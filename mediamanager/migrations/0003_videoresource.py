# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0002_auto_20150225_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoResource',
            fields=[
                ('defaultresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mediamanager.DefaultResource')),
                ('videofile', models.FileField(upload_to=b'static/videofile/%Y/%m/%d')),
            ],
            options={
            },
            bases=('mediamanager.defaultresource',),
        ),
    ]
