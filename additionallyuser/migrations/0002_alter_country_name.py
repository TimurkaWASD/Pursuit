# Generated by Django 5.0.3 on 2024-04-09 08:41

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('additionallyuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
