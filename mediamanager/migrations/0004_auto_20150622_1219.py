# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0003_auto_20150619_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultresource',
            name='agebracket',
            field=models.ManyToManyField(to='mediamanager.AgeBracket', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultresource',
            name='level',
            field=models.ManyToManyField(to='mediamanager.AssoeLevel', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultresource',
            name='pathway',
            field=models.ManyToManyField(to='mediamanager.AssoePathway', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultresource',
            name='subject',
            field=models.ManyToManyField(to='mediamanager.AssoeSubjects', db_index=True),
            preserve_default=True,
        ),
    ]
