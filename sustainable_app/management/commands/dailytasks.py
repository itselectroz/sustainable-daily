from django.core.management.base import BaseCommand

from ...models import DailyGoalStatus, Goal, QuizQuestion, User

import datetime


class Command(BaseCommand):
    """
    A class for handling daily tasks (used by django, has to be called Command)
    """
    help = 'Run all daily tasks.'


    def handle(self, *args, **options):
        """
        Function run when command is called
        """

        # Runs at 11:55 every day
        self.today = datetime.date.today()

        self.stdout.write(
            f"Starting daily tasks for {self.today.strftime('%Y-%m-%d')}.")

        self.calculate_minigame_points()

        self.randomize_daily_goals()

        self.reset_streaks()

    # Task functions

    def calculate_minigame_points(self):
        """
        Calculates the points that a user gets from all of the goals they have completed and adds it to the users points
        """
        try:

            daily_goals = DailyGoalStatus.objects.filter(
                user_data__date=self.today, completed=True, score__gt=0)

            for daily_goal in daily_goals:
                user = daily_goal.user_data.user
                user.points += max(daily_goal.score * 10, 500)

            self.stdout.write(self.style.SUCCESS(
                "[calculate_minigame_points] Task completed successfully."))

        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR(
                "[calculate_minigame_points] Something went wrong."))

    def randomize_daily_goals(self):
        """
        Sets 5 random daily goals that will appear on the home page of users for the next day
        
        Will be at least one minigame and one location task then 3 random tasks
        """
        # Set 5 random daily goals to active
        u_goals = Goal.objects.exclude(type=Goal.PERSONAL)

        # Setting all goals to inactive
        for goal in u_goals:
            goal.active = False
            goal.save()

        # Choose a random minigame and a random location task
        # Looks for minigame and location task individually in case one cannot be found
        try:
            minigame = Goal.objects.filter(
                type=Goal.MINIGAME).order_by('?').first()
            if minigame is not None:
                minigame.active = True
                minigame.save()
        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR(
                "[randomize_daily_goals] Something went wrong."))

        try:
            location_task = Goal.objects.filter(
                type=Goal.LOCATION).order_by('?').first()
            if location_task is not None:
                location_task.active = True
                location_task.save()
        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR(
                "[randomize_daily_goals] Something went wrong."))

        try:
            id_array = []

            try:
                id_array.append(minigame.id)
            except Exception:
                self.stdout.write(
                    "[randomize_daily_goals] Cannot find a minigame")

            try:
                id_array.append(location_task.id)
            except Exception:
                self.stdout.write(
                    "[randomize_daily_goals] Cannot find location task")

            new_goals = Goal.objects.exclude(
                id__in=id_array).exclude(type=Goal.PERSONAL)

            if QuizQuestion.objects.count() == 0:
                new_goals = new_goals.exclude(type=Goal.QUIZ)

            new_goals = new_goals.order_by('?')[:3]

            for goal in new_goals:
                goal.active = True
                goal.save()

            self.stdout.write(self.style.SUCCESS(
                "[randomize_daily_goals] Task completed successfully."))

        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR(
                "[randomize_daily_goals] Something went wrong."))

    def reset_streaks(self):
        """
        Will reset a users streak to 0 if they havent completed a task in the previous day 
        """
        try:
            users = User.objects.filter(
                date_last_task_completed__lt=self.today)

            for user in users:
                user.streak_length = 0
                user.save()
            
            self.stdout.write(self.style.SUCCESS(
                "[reset_streaks] Task completed successfully."))

        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR(
                "[reset_streaks] Something went wrong."))
