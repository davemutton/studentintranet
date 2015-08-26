# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0004_auto_20150622_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultresource',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 0, 24, 34, 155962, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
