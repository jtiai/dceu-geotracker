# Generated by Django 2.1.7 on 2019-04-01 16:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouteLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326)),
                ('color', models.CharField(default='#a0a0a0', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='TrackedPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
