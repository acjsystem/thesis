# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsys', '0004_auto_20170807_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='ignition_stat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='taser_stat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='rep_photo',
            field=models.FileField(upload_to=''),
        ),
    ]
