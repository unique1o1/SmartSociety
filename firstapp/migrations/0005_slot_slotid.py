# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20170204_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='slotid',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
