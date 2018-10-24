# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20181019_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttask',
            name='closing_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projecttask',
            name='earliest_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
