# Generated by Django 4.2.4 on 2023-08-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0002_alter_bussiness_hour_store_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussiness_hour',
            name='end_time_local',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussiness_hour',
            name='start_time_local',
            field=models.CharField(max_length=255),
        ),
    ]
