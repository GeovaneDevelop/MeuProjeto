# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 16:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170210_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagens',
            name='data_publicada',
            field=models.DateField(default=datetime.datetime(2017, 2, 10, 16, 48, 34, 259411, tzinfo=utc)),
        ),
    ]
