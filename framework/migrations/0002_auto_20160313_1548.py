# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 19:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendaruser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userPointer', to=settings.AUTH_USER_MODEL),
        ),
    ]
