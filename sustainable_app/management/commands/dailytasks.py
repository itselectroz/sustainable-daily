from django.core.management.base import BaseCommand

import datetime


class Command(BaseCommand):
    help = 'Run all daily tasks.'

    def handle(self, *args, **options):
        today = datetime.date.today()
        self.stdout.write(
            f"Starting daily tasks for {today.strftime('%Y-%m-%d')}.")

        self.calculate_minigame_points()

    # Task functions

    def calculate_minigame_points(self):
        pass
