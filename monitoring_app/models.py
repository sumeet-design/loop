from django.db import models
from django.utils import timezone
class store_status(models.Model):
    store_id = models.CharField(max_length=255)
    timestamp_utc = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10)

class bussiness_hour(models.Model):
    store_id = models.CharField(max_length=255)
    day_of_week = models.IntegerField()
    start_time_local = models.CharField(max_length=255)
    end_time_local = models.CharField(max_length=255)

class store_data(models.Model):
    store_id = models.CharField(max_length=255)
    timezone_str = models.CharField(max_length=50,default='America/Chicago')


class Report(models.Model):
    report_id = models.CharField(max_length=50,null=False)
    csv_file = models.FileField(upload_to='reports/')  # Specify the upload path
