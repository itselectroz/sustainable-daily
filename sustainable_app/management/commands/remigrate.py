from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    """
    A class for handling remigration
    """
    help = 'A command to rerun all migrations.'

    def handle(self, *args, **options):
        """
        Rolls back all migrations and remigrates
        """
        try:
            self.stdout.write("Rolling back all migrations...")
            call_command('migrate', 'sustainable_app', 'zero')
            self.stdout.write(self.style.SUCCESS(
                'Successfully rolled back migrations.'))
            call_command('migrate', 'sustainable_app')
            self.stdout.write(self.style.SUCCESS(
                'Successfully re-migrated database.'))
        except CommandError as e:
            self.stdout.write(self.style.ERROR('Something went wrong:'))
            self.stderr.write(str(e))
