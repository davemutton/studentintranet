# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defaultresource',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='defaultresource',
            name='upvotes',
        ),
    ]
