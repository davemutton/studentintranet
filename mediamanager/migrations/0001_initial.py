# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('filemanage', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeBracket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agebracket', models.CharField(max_length=25)),
                ('order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssoeLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=25)),
                ('order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssoePathway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pathway', models.CharField(max_length=1)),
                ('order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssoeSubjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=55)),
                ('order', models.IntegerField()),
                ('slug', models.SlugField(max_length=100, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefaultResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, editable=False, blank=True)),
                ('views', models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True)),
                ('score', models.DecimalField(default=0, max_digits=20, decimal_places=4, blank=True)),
                ('icon', models.CharField(max_length=254, editable=False, blank=True)),
                ('description', models.TextField(blank=True)),
                ('updownvotes_likes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('updownvotes_dislikes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileResource',
            fields=[
                ('defaultresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mediamanager.DefaultResource')),
                ('files', models.ManyToManyField(to='filemanage.AttachedFiles', blank=True)),
            ],
            options={
            },
            bases=('mediamanager.defaultresource',),
        ),
        migrations.CreateModel(
            name='LearningObject',
            fields=[
                ('defaultresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mediamanager.DefaultResource')),
                ('archivefile', models.FileField(upload_to=b'static/learningobject/archivefiles/%Y/%m/%d')),
                ('indexpath', models.CharField(max_length=254, editable=False, blank=True)),
            ],
            options={
            },
            bases=('mediamanager.defaultresource',),
        ),
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
        migrations.CreateModel(
            name='VideoResource',
            fields=[
                ('defaultresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mediamanager.DefaultResource')),
                ('videofile', models.FileField(upload_to=b'videofile/%Y/%m/%d')),
            ],
            options={
            },
            bases=('mediamanager.defaultresource',),
        ),
        migrations.AddField(
            model_name='defaultresource',
            name='agebracket',
            field=models.ManyToManyField(to='mediamanager.AgeBracket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='defaultresource',
            name='level',
            field=models.ManyToManyField(to='mediamanager.AssoeLevel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='defaultresource',
            name='pathway',
            field=models.ManyToManyField(to='mediamanager.AssoePathway'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='defaultresource',
            name='subject',
            field=models.ManyToManyField(to='mediamanager.AssoeSubjects'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='defaultresource',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
