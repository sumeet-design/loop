import csv
from datetime import datetime
from pytz import timezone
from django.core.management.base import BaseCommand
from monitoring_app.models import StoreTimezone, BusinessHours, StoreStatus

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Import Store data
        # with open('store_data.csv', 'r') as store_file:
        #     # store_data = csv.reader(store_file)
        #     store_data = csv.DictReader(store_file)
        #     for row in store_data:
        #         print("here is the value of row",row)
        #         #break
        #         store_id = row['store_id'] 
        #         timezone_str = row['timezone_str']
        #         StoreTimezone.objects.create(store_id=store_id, timezone_str=timezone_str)

        # Import StoreBusinessHours data
        # with open('business_hours.csv', 'r') as hours_file:
        #     hours_data = csv.DictReader(hours_file)
        #     for row in hours_data:
        #         print("here is the value of bussiness row",row)
        #         store_id = row['store_id']
        #         day_of_week = row['day'] 
        #         start_time_local = row['start_time_local'] 
        #         end_time_local = row['end_time_local']
        #         #break
        #         BusinessHours.objects.create(
        #             store_id=store_id,
        #             day_of_week=day_of_week,
        #             start_time_local=start_time_local,
        #             end_time_local=end_time_local
        #         )

        # Import StoreStatus data
        with open('store_status.csv', 'r') as status_file:
            status_data = csv.DictReader(status_file)
            for row in status_data:
                store_id = row['store_id']
                timestamp_utc_str = row['timestamp_utc']  # Assuming the format is "YYYY-MM-DD HH:MM:SS.uuuuuu UTC"
                timestamp_utc = datetime.strptime(timestamp_utc_str, '%Y-%m-%d %H:%M:%S.%f UTC')
                status = row['status']
                StoreStatus.objects.create(
                    store_id=store_id,
                    timestamp_utc=timestamp_utc,
                    status=status
                )
