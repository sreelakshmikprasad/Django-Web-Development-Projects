# Generated by Django 4.1.7 on 2023-05-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('May', '0002_productdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
