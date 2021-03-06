# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0013_auto_20171023_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='data',
            name='edited_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('Tourist', 'Tourist'), ('Business', 'Business'), ('Student', 'Student')], max_length=15),
        ),
    ]
