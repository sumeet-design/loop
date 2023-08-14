from django.core.management.base import BaseCommand
from monitoring_app.models import StoreTimezone

class Command(BaseCommand):
    help = 'Load sample store timezone data'

    def handle(self, *args, **kwargs):
        sample_data = [
            (1, 'America/New_York'),
            (2, 'America/Los_Angeles'),
            (3, 'America/Chicago'),
            # ... Add more sample data here
        ]

        for data in sample_data:
            store_id, timezone_str = data
            StoreTimezone.objects.create(store_id=store_id, timezone_str=timezone_str)

        self.stdout.write(self.style.SUCCESS('Sample store timezone data loaded successfully'))
