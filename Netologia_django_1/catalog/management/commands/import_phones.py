import csv
from django.core.management.base import BaseCommand
from catalog.models import Phone
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import phones from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone, created = Phone.objects.update_or_create(
                    id=row['id'],
                    defaults={
                        'name': row['name'],
                        'price': row['price'],
                        'image': row['image'],
                        'release_date': parse_date(row['release_date']),
                        'lte_exists': row['lte_exists'] == 'True'
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created phone: {phone.name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated phone: {phone.name}'))
