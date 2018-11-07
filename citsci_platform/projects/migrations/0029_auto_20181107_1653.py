# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20181029_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='testing_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.UserGroup'),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='testing_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.UserGroup'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verification_token',
            field=models.UUIDField(default=uuid.UUID('f81da50e-0c39-4252-bd98-6197c37d8a38'), editable=False, null=True),
        ),
    ]