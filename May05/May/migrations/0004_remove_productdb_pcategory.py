# Generated by Django 4.1.7 on 2023-05-16 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('May', '0003_productdb_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdb',
            name='PCategory',
        ),
    ]
