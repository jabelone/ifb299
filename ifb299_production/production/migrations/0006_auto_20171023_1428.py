# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_auto_20171006_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='link',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='map_link',
            field=models.CharField(default='null', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
