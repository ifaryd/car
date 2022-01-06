# Generated by Django 2.2.14 on 2022-01-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20220105_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='photo_arriere',
            field=models.ImageField(blank=True, default='app/static/images/logo-light.png', null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='photo_face',
            field=models.ImageField(blank=True, default='app/static/images/logo-light.png', null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='photo_longueur1',
            field=models.ImageField(blank=True, default='app/static/images/logo-light.png', null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='photo_longueur2',
            field=models.ImageField(blank=True, default='app/static/images/logo-light.png', null=True, upload_to='media/images/'),
        ),
    ]
