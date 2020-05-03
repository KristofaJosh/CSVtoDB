# Generated by Django 2.2.12 on 2020-05-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetRequestActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=6)),
                ('url', models.CharField(max_length=1024)),
                ('timeStamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZenoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('csv_temperature', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('csv_timestamp', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('csv_duration', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
    ]
