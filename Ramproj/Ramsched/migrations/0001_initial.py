# Generated by Django 4.0.3 on 2022-04-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newClientName', models.TextField(blank=True)),
                ('newClientphoneNo', models.TextField(blank=True)),
                ('newtimeSession', models.TextField(blank=True)),
            ],
        ),
    ]
