# Generated by Django 4.0.4 on 2022-06-27 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ilano_app', '0002_rename_customerinfo_customerinformations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cus_Name', models.TextField(blank=True)),
                ('Cus_Contact', models.TextField(blank=True)),
                ('Cus_Address', models.TextField(blank=True)),
                ('Cus_Email', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pro_Name', models.TextField(blank=True)),
                ('Pro_Amount', models.TextField(blank=True)),
                ('Pro_Price', models.TextField(blank=True)),
                ('Pro_Detail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rev_Comment', models.TextField(blank=True)),
                ('Rev_Suggestion', models.TextField(blank=True)),
                ('Cus_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ilano_app.customer')),
                ('Pro_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ilano_app.products')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ord_Date', models.DateField()),
                ('Ord_Price', models.TextField(blank=True)),
                ('Ord_Detail', models.TextField(blank=True)),
                ('Ord_Status', models.TextField(blank=True)),
                ('Cus_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ilano_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Del_Detail', models.TextField(blank=True)),
                ('Del_Price', models.TextField(blank=True)),
                ('Del_Date', models.DateField()),
                ('Cus_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ilano_app.customer')),
                ('Ord_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ilano_app.order')),
                ('Pro_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ilano_app.products')),
            ],
        ),
    ]