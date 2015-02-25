# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultresource',
            old_name='score',
            new_name='upvotes',
        ),
        migrations.AddField(
            model_name='defaultresource',
            name='downvotes',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='defaultresource',
            name='views',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultresource',
            name='agebracket',
            field=models.ManyToManyField(to='mediamanager.AgeBracket'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultresource',
            name='level',
            field=models.ManyToManyField(to='mediamanager.AssoeLevel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultresource',
            name='pathway',
            field=models.ManyToManyField(to='mediamanager.AssoePathway'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultresource',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
