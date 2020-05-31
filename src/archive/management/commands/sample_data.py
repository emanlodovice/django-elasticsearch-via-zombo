from django.core.management.base import BaseCommand, CommandError
from archive.models import ArchiveZombo, Archive

from faker import Faker

class Command(BaseCommand):
    help = 'Generate fake data'

    def add_arguments(self, parser):
        parser.add_argument('number', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        f = Faker()
        archives = []
        archives_zombo = []
        for x in range(options['number']):
            name = f.name()
            content = f.text()
            archives.append(Archive(name=name, content=content))
            archives_zombo.append(ArchiveZombo(name=name, content=content))

        ArchiveZombo.objects.bulk_create(archives_zombo)
        Archive.objects.bulk_create(archives)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(archives)} Archives and {len(archives_zombo)} ArchiveZombos'))
