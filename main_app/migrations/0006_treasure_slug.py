# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_treasure_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
