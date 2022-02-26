# Generated by Django 4.0.2 on 2022-02-26 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SettingsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueDetails',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('issue_qty', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IssueMaster',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('issue_no', models.CharField(max_length=100, unique=True)),
                ('issue_to', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qty', models.FloatField()),
                ('rate', models.FloatField()),
                ('total', models.FloatField(default=0, editable=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SettingsApp.purchaseitems')),
            ],
            options={
                'verbose_name_plural': 'Purchase Details',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Vendor Details',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('receive_quantity', models.FloatField(blank=True, default='0', null=True)),
                ('issue_quantity', models.FloatField(blank=True, default='0', null=True)),
                ('stock_quantity', models.FloatField()),
                ('issue', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='PurchaseApp.issuedetails')),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SettingsApp.purchaseitems')),
                ('purchase', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='PurchaseApp.purchasedetails')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseMaster',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('invoice_no', models.CharField(max_length=100, unique=True)),
                ('total_bill', models.FloatField(default=0)),
                ('vendor', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='PurchaseApp.vendor')),
            ],
            options={
                'verbose_name_plural': 'Purchase Master',
            },
        ),
        migrations.AddField(
            model_name='purchasedetails',
            name='purchase_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PurchaseApp.purchasemaster'),
        ),
        migrations.AddField(
            model_name='purchasedetails',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SettingsApp.unit'),
        ),
        migrations.AddField(
            model_name='issuedetails',
            name='issue_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PurchaseApp.issuemaster'),
        ),
        migrations.AddField(
            model_name='issuedetails',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SettingsApp.purchaseitems'),
        ),
    ]
