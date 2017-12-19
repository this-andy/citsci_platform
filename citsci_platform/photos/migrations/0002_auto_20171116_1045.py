# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-16 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='file_location',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]