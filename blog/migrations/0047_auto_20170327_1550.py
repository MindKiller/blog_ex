# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20170327_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='author',
            new_name='authors',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='subscriber',
            new_name='subscribers',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='feed',
            field=models.ManyToManyField(default=0, related_name='feed', to='blog.Page'),
        ),
    ]
