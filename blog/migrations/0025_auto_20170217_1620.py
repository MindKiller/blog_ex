# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20170217_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='male.jpg', upload_to='profile_images'),
        ),
    ]
