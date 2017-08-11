# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carsys', '0008_auto_20170811_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='car_loc_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='car_photo_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
