from django.db import models

import datetime

from . import Goal


class DailyData(models.Model):
    date = models.DateField(primary_key=True, default=datetime.date.today)

    # Completions
    personal_goals = models.ManyToManyField(
        Goal, through='PersonalGoalStatus', related_name='personal_goals')
    daily_goals = models.ManyToManyField(
        Goal, through='DailyGoalStatus', related_name='daily_goals')

    def xp_reward(self):
        """
        Calculates the total XP reward for this user's
        completed daily goals.
        """
        completed_goals = self.daily_goals.filter(
            dailygoalstatus__completed=True
        )
        goal_sums = completed_goals.aggregate(
            total_xp_reward=models.Sum('xp_reward')
        )

        return goal_sums['total_xp_reward'] or 0

    def point_reward(self):
        """
        Calculates the total point reward for this user's
        completed daily goals.
        """
        completed_goals = self.daily_goals.filter(
            dailygoalstatus__completed=True
        )
        goal_sums = completed_goals.aggregate(
            total_point_reward=models.Sum('point_reward')
        )

        return goal_sums['total_point_reward'] or 0

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')}"

    @staticmethod
    def complete_goal(goal):
        """
        Adds a goal to the completed daily goals for today's date.

        If there is no `DailyData` instance for today's date, a new one is created.

        :param goal: A `Goal` instance to be added to today's daily goals.
        :type goal: `Goal`
        """
        # Get daily data
        daily_data, _ = DailyData.objects.get_or_create(
            date=datetime.date.today()
        )

        # Get goal status
        daily_status, _ = DailyGoalStatus.objects.get_or_create(
            goal=goal,
            user_data=daily_data,
        )

        # Mark as completed
        daily_status.completed = True
        daily_status.save()

    @staticmethod
    def complete_personal_goal(goal):
        """
        Adds a goal to the completed personal goals for today's date.

        If there is no `DailyData` instance for today's date, a new one is created.

        :param goal: A `Goal` instance to be added to today's personal goals.
        :type goal: `Goal`
        """
        # Get daily data
        daily_data, _ = DailyData.objects.get_or_create(
            date=datetime.date.today()
        )

        # Get goal status
        personal_goal_status, _ = PersonalGoalStatus.objects.get_or_create(
            goal=goal,
            user_data=daily_data,
        )

        # Mark as completed
        personal_goal_status.completed = True
        personal_goal_status.save()


class PersonalGoalStatus(models.Model):
    user_data = models.ForeignKey(DailyData, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)


class DailyGoalStatus(models.Model):
    user_data = models.ForeignKey(DailyData, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    score = models.IntegerField(default=0)

    def xp_reward(self):
        return self.goal.xp_reward or 0

    def point_reward(self):
        return self.goal.point_reward or 0
