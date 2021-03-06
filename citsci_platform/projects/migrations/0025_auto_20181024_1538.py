# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20181024_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttask',
            name='signup_status',
            field=models.CharField(choices=[('not-open', 'Not yet open'), ('open', 'Open'), ('closed', 'Closed')], default='open', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='status',
            field=models.CharField(choices=[('planned', 'Planned'), ('testing', 'Testing'), ('active', 'Active'), ('complete', 'Complete')], default='active', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=12),
            preserve_default=False,
        ),
    ]
