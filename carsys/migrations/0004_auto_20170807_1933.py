# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carsys', '0003_auto_20170807_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='rep_person',
            new_name='rep_photo',
        ),
    ]