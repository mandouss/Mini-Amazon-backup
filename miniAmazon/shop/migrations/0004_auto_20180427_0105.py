# Generated by Django 2.0 on 2018-04-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180427_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(blank=True, default='good', upload_to='good/'),
        ),
    ]
