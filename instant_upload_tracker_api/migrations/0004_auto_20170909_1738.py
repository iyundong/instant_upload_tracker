# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-09 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instant_upload_tracker_api', '0003_auto_20170820_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iubugtracker',
            name='android_device_info',
            field=models.CharField(max_length=255, verbose_name='Build.BRAND + Build.DEVICE + Build.MODEL'),
        ),
        migrations.AlterField(
            model_name='iudeviceinfotracker',
            name='android_device_info',
            field=models.CharField(max_length=255, verbose_name='Build.BRAND + Build.DEVICE + Build.MODEL'),
        ),
    ]
