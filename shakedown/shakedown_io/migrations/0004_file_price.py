# Generated by Django 2.2 on 2020-12-14 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakedown_io', '0003_auto_20201213_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='price',
            field=models.IntegerField(default=0, max_length='5'),
            preserve_default=False,
        ),
    ]
