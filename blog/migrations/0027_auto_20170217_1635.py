# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20170217_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='avatar.jpg', height_field='200px', upload_to='profile_images', width_field='200px'),
        ),
    ]
