# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('slug', models.SlugField()),
                ('parent_category', models.ForeignKey(blank=True, to='agency.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('code', models.IntegerField(default=0)),
                ('adres', models.CharField(max_length=256, null=True)),
                ('body', tinymce.models.HTMLField()),
                ('phone', models.CharField(unique=True, max_length=128)),
                ('room', models.IntegerField(blank=True)),
                ('square', models.IntegerField(blank=True)),
                ('price', models.IntegerField(default=0, max_length=64)),
                ('picture1', models.ImageField(upload_to=b'', blank=True)),
                ('picture2', models.ImageField(upload_to=b'', blank=True)),
                ('picture3', models.ImageField(upload_to=b'', blank=True)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(to='agency.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Headermenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('url', models.CharField(unique=True, max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=256)),
                ('slug', models.SlugField()),
                ('body', tinymce.models.HTMLField()),
                ('keyword', models.CharField(max_length=256, unique=True, null=True)),
                ('description', models.CharField(max_length=256, unique=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
