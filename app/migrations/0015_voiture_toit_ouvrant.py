# Generated by Django 2.2.14 on 2022-01-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220105_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='toit_ouvrant',
            field=models.BooleanField(default=False),
        ),
    ]