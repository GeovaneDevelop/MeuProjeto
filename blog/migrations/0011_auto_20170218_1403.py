# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-18 14:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170218_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagens',
            name='data_publicada',
            field=models.DateField(default=datetime.datetime(2017, 2, 18, 14, 3, 47, 86598, tzinfo=utc)),
        ),
    ]
