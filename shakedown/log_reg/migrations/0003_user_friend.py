# Generated by Django 2.2 on 2020-11-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0002_user_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friend',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_friend_+', to='log_reg.User'),
        ),
    ]
