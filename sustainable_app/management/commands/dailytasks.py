from django.core.management.base import BaseCommand

from ...models import DailyGoalStatus, Goal

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

        self.randomize_daily_goals()

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
            
    def randomize_daily_goals(self) :
        #Set 5 random daily goals to active
        u_goals = Goal.objects.exclude(type=Goal.PERSONAL)

        #Setting all goals to inactive 
        for goal in u_goals:
            goal.active = False
            goal.save()
        
        #Setting 5 random goals to active, needs to have 5 for it to work
        #new_goals = u_goals.order_by('?')[:2]

        
        # Choose a random minigame and a random location task
        # Looks for minigame and location task individually in case one cannot be found
        try:
            minigame = Goal.objects.filter(type=Goal.MINIGAME).order_by('?').first()
            minigame.active = True
            minigame.save()
        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR("[randomize_daily_goals] Something went wrong."))


        try:
            location_task = Goal.objects.filter(type=Goal.LOCATION).order_by('?').first()
            location_task.active = True
            location_task.save()
        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR("[randomize_daily_goals] Something went wrong."))


            
        try:
            id_array = []
            
            try:
                id_array.push(minigame.id)
            except:
                self.stdout.write("Cannot find a minigame")

            try:
                id_array.push(location_task.id)
            except:
                self.stdout.write("Cannot find location task")

            new_goals = Goal.objects.exclude(id__in = id_array).order_by('?')[:1]

            for goal in new_goals:
                goal.active = True
                goal.save()

        except Exception as e:
            self.stdout.write(str(e))
            self.stdout.write(self.style.ERROR("[randomize_daily_goals] Something went wrong."))


        

