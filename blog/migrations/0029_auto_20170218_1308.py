# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20170218_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.CharField(max_length=254),
        ),
    ]
