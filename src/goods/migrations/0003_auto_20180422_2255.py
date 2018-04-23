# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-22 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import goods.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_good_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=goods.models.upload_image_path),
        ),
    ]