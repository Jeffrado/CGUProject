# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_profile_profileimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='pinyinType',
            field=models.IntegerField(default=0),
        ),
    ]