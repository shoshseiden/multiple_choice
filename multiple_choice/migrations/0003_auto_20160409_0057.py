# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiple_choice', '0002_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='incorrect_answer_1',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='incorrect_answer_2',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='incorrect_answer_3',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
