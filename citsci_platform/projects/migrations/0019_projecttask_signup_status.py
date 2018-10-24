# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20181022_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttask',
            name='signup_status',
            field=models.CharField(blank=True, choices=[('not-open', 'Not yet open'), ('open', 'Open'), ('invitation', 'Invitation only'), ('closed', 'Closed')], max_length=12, null=True),
        ),
    ]
