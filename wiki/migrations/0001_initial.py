# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdminPage',
            fields=[
                ('defaultpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wiki.DefaultPage')),
                ('body', models.TextField(blank=True)),
            ],
            options={
            },
            bases=('wiki.defaultpage',),
        ),
        migrations.CreateModel(
            name='LearningObject',
            fields=[
                ('defaultpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wiki.DefaultPage')),
                ('archivefile', models.FileField(upload_to=b'static/learningobject/archivefiles/%Y/%m/%d')),
                ('indexpath', models.CharField(max_length=254, editable=False)),
            ],
            options={
            },
            bases=('wiki.defaultpage',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('defaultpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wiki.DefaultPage')),
                ('body', models.TextField(blank=True)),
            ],
            options={
            },
            bases=('wiki.defaultpage',),
        ),
        migrations.CreateModel(
            name='SubjectPage',
            fields=[
                ('defaultpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wiki.DefaultPage')),
            ],
            options={
            },
            bases=('wiki.defaultpage',),
        ),
        migrations.AddField(
            model_name='defaultpage',
            name='parent_page',
            field=models.ForeignKey(blank=True, to='wiki.DefaultPage', null=True),
            preserve_default=True,
        ),
    ]
