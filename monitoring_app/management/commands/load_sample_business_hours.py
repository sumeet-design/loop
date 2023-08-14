from django.core.management.base import BaseCommand
from monitoring_app.models import BusinessHours

class Command(BaseCommand):
    help = 'Load sample business hours data'

    def handle(self, *args, **kwargs):
        sample_data = [
            (1, 0, '09:00:00', '18:00:00'),
            (2, 1, '08:00:00', '20:00:00'),
            (3, 2, '10:00:00', '15:00:00'),
            # ... Add more sample data here
        ]

        for data in sample_data:
            store_id, day_of_week, start_time_local, end_time_local = data
            BusinessHours.objects.create(store_id=store_id, day_of_week=day_of_week, start_time_local=start_time_local, end_time_local=end_time_local)

        self.stdout.write(self.style.SUCCESS('Sample business hours data loaded successfully'))
