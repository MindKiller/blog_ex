# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 14:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0032_auto_20170218_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='favorite',
        ),
        migrations.AddField(
            model_name='page',
            name='favorite',
            field=models.ManyToManyField(default=0, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
