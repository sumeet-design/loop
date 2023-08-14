# Generated by Django 4.2.4 on 2023-08-13 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bussiness_hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('day_of_week', models.IntegerField()),
                ('start_time_local', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time_local', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.CharField(max_length=50)),
                ('csv_file', models.FileField(upload_to='reports/')),
            ],
        ),
        migrations.CreateModel(
            name='store_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('timezone_str', models.CharField(default='America/Chicago', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='store_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('timestamp_utc', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]