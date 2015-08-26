# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0005_defaultresource_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defaultresource',
            name='pub_date',
        ),
    ]
