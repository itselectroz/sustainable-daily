from django.core.management.base import BaseCommand

from ...models import DailyGoalStatus

import datetime


class Command(BaseCommand):
    help = 'Run all daily tasks.'

    def handle(self, *args, **options):
        # This code will run sometime around midnight,
        # but not necessarily before or after.
        # To account for this, we need to calculate the correct day.
        now = datetime.datetime.now()
        if now.hour < 12:
            self.today = datetime.date.today() - datetime.timedelta(days=1)
        else:
            self.today = datetime.date.today()

        self.stdout.write(
            f"Starting daily tasks for {self.today.strftime('%Y-%m-%d')}.")

        self.calculate_minigame_points()

    # Task functions

    def calculate_minigame_points(self):
        try:
            today = datetime.date.today()

            daily_goals = DailyGoalStatus.objects.filter(
                user_data__date=today, completed=True, score__gt=0)

            for daily_goal in daily_goals:
                user = daily_goal.user_data.user
                user.points += max(daily_goal.score * 10, 500)

            self.stdout.write(self.style.SUCCESS(
                "[calculate_minigame_points] Task completed successfully."))

        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR(
                "[calculate_minigame_points] Something went wrong."))
