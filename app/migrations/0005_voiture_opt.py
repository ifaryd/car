# Generated by Django 2.2.14 on 2021-11-12 11:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211031_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='opt',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Value1'), (2, 'Value2'), (3, 'Value3'), (4, 'Value4'), (5, 'Value5')], default=None, max_length=3),
            preserve_default=False,
        ),
    ]
