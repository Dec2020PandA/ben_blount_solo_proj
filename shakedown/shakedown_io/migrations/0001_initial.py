# Generated by Django 2.2 on 2020-12-13 18:38

from django.db import migrations, models
import django.db.models.deletion
import shakedown_io.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_reg', '0004_auto_20201208_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_reg.User')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.FileField(upload_to=shakedown_io.models.user_directory_path)),
                ('name', models.CharField(max_length=45)),
                ('code', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shakedown_io.Client')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_reg.User')),
            ],
        ),
    ]
