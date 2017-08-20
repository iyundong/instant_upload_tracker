# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-20 10:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instant_upload_tracker_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iudeviceinfotracker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now(), verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iudeviceinfotracker',
            name='device_id',
            field=models.IntegerField(default=0, verbose_name='设备id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iudeviceinfotracker',
            name='lib_version',
            field=models.IntegerField(default=0, verbose_name='所使用的库的版本'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iudeviceinfotracker',
            name='vender_id',
            field=models.IntegerField(default=0, verbose_name='厂商id'),
            preserve_default=False,
        ),
    ]
