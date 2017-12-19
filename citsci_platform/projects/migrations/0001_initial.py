# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-30 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=20)),
            ],
        ),
    ]
