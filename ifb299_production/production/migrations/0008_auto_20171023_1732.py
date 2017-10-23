# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0007_auto_20171023_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='image_link',
            field=models.TextField(default='https://blank'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='data_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='link',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='data',
            name='map_link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
