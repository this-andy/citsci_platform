# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-23 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20171116_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]