# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20170323_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pages',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Page'),
        ),
    ]
