# Generated by Django 3.2 on 2021-04-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0002_auto_20210423_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data_matched',
        ),
        migrations.AddField(
            model_name='post',
            name='ties',
            field=models.IntegerField(default=0),
        ),
    ]
