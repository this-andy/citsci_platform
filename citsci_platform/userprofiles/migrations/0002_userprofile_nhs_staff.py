# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-22 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nhs_staff',
            field=models.NullBooleanField(default=None),
        ),
    ]
