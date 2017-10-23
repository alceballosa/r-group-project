# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='photo_url',
        ),
        migrations.AddField(
            model_name='person',
            name='model_pic',
            field=models.ImageField(default='static/img/user-male-default.png', upload_to='static/img/persons'),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
