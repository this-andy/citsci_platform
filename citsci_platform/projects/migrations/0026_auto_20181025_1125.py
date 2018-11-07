# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20181024_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='testing_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.UserGroup'),
        ),
        migrations.AddField(
            model_name='projecttask',
            name='testing_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.UserGroup'),
        ),
    ]