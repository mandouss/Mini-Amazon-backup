# Generated by Django 2.0 on 2018-04-27 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20180427_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(blank=True, default='good', upload_to='product/915641_in_pp_ioZkcDv.jpg'),
        ),
    ]
