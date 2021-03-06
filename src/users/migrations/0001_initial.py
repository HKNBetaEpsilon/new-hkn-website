# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 23:54
from __future__ import unicode_literals

import users.models

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('uniqname', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('status',
                 models.CharField(choices=[('A', 'Active'), ('E', 'Electee'), ('O', 'Officer')],
                                  default='E', max_length=1)),
                ('major', models.CharField(blank=True, choices=[('CS', 'Computer Science'),
                                                                ('CE', 'Computer Engineering'),
                                                                ('EE', 'Electrical Engineering')],
                                           max_length=2, null=True)),
                ('edu_level', models.CharField(blank=True,
                                               choices=[('UG', 'Undergraduate'), ('GR', 'Graduate'),
                                                        ('AL', 'Alumni')], max_length=2,
                                               null=True)),
                ('expected_grad_date', models.DateField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True,
                                                  upload_to=users.models.user_directory_path)),
                ('resume', models.FileField(blank=True, null=True,
                                            upload_to=users.models.user_directory_path)),
            ],
            options={
                'ordering': ['uniqname'],
            },
        ),
    ]
