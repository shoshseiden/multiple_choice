# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-06 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiple_choice', '0003_auto_20160830_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='correct_answer',
            field=models.CharField(default=' ', max_length=25),
            preserve_default=False,
        ),
    ]
