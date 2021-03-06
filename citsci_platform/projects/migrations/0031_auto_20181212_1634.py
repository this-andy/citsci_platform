# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-12 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_auto_20181208_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttask',
            name='external_system_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ExternalSystem'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verification_token',
            field=models.UUIDField(default=uuid.UUID('36caac1d-8916-4706-8909-63c2603d0b00'), editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='userexternalaccount',
            name='external_user_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
