# Generated by Django 2.2.14 on 2021-12-24 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211224_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voiture',
            old_name='date_ajout',
            new_name='date_ajouts',
        ),
    ]
