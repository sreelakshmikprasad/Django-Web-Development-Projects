# Generated by Django 4.1.7 on 2023-06-15 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('May', '0005_contactsdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FName', models.CharField(blank=True, max_length=50, null=True)),
                ('LName', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Phone', models.CharField(blank=True, max_length=50, null=True)),
                ('AddrsLine1', models.CharField(blank=True, max_length=50, null=True)),
                ('AddrsLine2', models.CharField(blank=True, max_length=50, null=True)),
                ('Country', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('PinCode', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
