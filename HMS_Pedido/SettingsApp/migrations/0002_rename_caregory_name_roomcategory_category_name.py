# Generated by Django 4.0.2 on 2022-02-21 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SettingsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomcategory',
            old_name='caregory_name',
            new_name='category_name',
        ),
    ]
