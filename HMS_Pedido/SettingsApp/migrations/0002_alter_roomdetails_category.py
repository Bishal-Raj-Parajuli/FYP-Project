# Generated by Django 4.0.2 on 2022-03-04 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SettingsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdetails',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SettingsApp.roomcategory'),
        ),
    ]