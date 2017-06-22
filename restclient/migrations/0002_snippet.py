# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-22 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restclient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(default='python', max_length=100)),
                ('style', models.CharField(default='friendly', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
