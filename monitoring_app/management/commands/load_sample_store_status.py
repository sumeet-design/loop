from django.core.management.base import BaseCommand
from monitoring_app.models import StoreStatus

class Command(BaseCommand):
    help = 'Load sample store status data'

    def handle(self, *args, **kwargs):
        sample_data = [
    (1, '2023-08-01 08:00:00', 'active'),
    (1, '2023-08-01 09:00:00', 'active'),
    (1, '2023-08-01 10:00:00', 'inactive'),
    (1, '2023-08-01 11:00:00', 'inactive'),
    (1, '2023-08-01 12:00:00', 'active'),
    (1, '2023-08-01 13:00:00', 'active'),
    (1, '2023-08-01 14:00:00', 'active'),
    (1, '2023-08-01 15:00:00', 'active'),
    (1, '2023-08-01 16:00:00', 'inactive'),
    (1, '2023-08-01 17:00:00', 'inactive'),
    (1, '2023-08-01 18:00:00', 'active'),
    (2, '2023-08-01 08:00:00', 'active'),
    (2, '2023-08-01 09:00:00', 'active'),
    (2, '2023-08-01 10:00:00', 'active'),
    (2, '2023-08-01 11:00:00', 'active'),
    (2, '2023-08-01 12:00:00', 'active'),
    (2, '2023-08-01 13:00:00', 'active'),
    (2, '2023-08-01 14:00:00', 'active'),
    (2, '2023-08-01 15:00:00', 'active'),
    (2, '2023-08-01 16:00:00', 'active'),
    (2, '2023-08-01 17:00:00', 'active'),
    (2, '2023-08-01 18:00:00', 'active'),
    (2, '2023-08-01 19:00:00', 'active'),
    (2, '2023-08-01 20:00:00', 'active'),
    (3, '2023-08-01 08:00:00', 'inactive'),
    (3, '2023-08-01 09:00:00', 'inactive'),
    (3, '2023-08-01 10:00:00', 'inactive'),
    (3, '2023-08-01 11:00:00', 'inactive'),
    (3, '2023-08-01 12:00:00', 'inactive'),
    (3, '2023-08-01 13:00:00', 'inactive'),
    (3, '2023-08-01 14:00:00', 'active'),
    (3, '2023-08-01 15:00:00', 'active'),
    (3, '2023-08-01 16:00:00', 'active'),
    (3, '2023-08-01 17:00:00', 'inactive'),
    (3, '2023-08-01 18:00:00', 'inactive'),
    (3, '2023-08-01 19:00:00', 'inactive'),
    (3, '2023-08-01 20:00:00', 'inactive'),
]


        for data in sample_data:
            store_id, timestamp_utc, status = data
            StoreStatus.objects.create(store_id=store_id, timestamp_utc=timestamp_utc, status=status)

        self.stdout.write(self.style.SUCCESS('Sample store status data loaded successfully'))
