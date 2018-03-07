# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-30 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('project_id', models.UUIDField(default=uuid.uuid4)),
                ('user_id', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]