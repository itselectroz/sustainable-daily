from django.db import models
from django.utils import timezone
from . import Goal


class DailyData(models.Model):
    date = models.DateField(primary_key=True, default=timezone.now)

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
        completed_goals = self.daily_goals.filter(completed=True)
        goal_sums = completed_goals.aggregate(
            total_xp_reward=models.Sum('xp_reward')
        )

        return goal_sums['total_xp_reward'] or 0

    def point_reward(self):
        """
        Calculates the total point reward for this user's
        completed daily goals.
        """
        completed_goals = self.daily_goals.filter(completed=True)
        goal_sums = completed_goals.aggregate(
            total_point_reward=models.Sum('point_reward')
        )

        return goal_sums['total_point_reward'] or 0

    def __str__(self):
        return str(self.date)


class PersonalGoalStatus(models.Model):
    user_data = models.ForeignKey(DailyData, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)


class DailyGoalStatus(models.Model):
    user_data = models.ForeignKey(DailyData, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)
    xp_reward = models.IntegerField(default=0)
    point_reward = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
