from django.db import models

import datetime

from . import Goal, User, Statistics


class DailyData(models.Model):
    """
    Daily data holds information about a users activities for a specific date
    Can return the xp and points a user has earned and the goals a user has completed on that day
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)

    # Completions
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
    def complete_goal(user, goal):
        """
        Adds a goal to a user's completed daily goals for today's date.

        If there is no `DailyData` instance for today's date, a new one is created.

        :param user: The `User` instance to complete the goal for.
        :type user: `User`
        :param goal: A `Goal` instance to be added to today's daily goals.
        :type goal: `Goal`
        """
        # Get daily data
        daily_data, _ = DailyData.objects.get_or_create(
            user=user,
            date=datetime.date.today()
        )

        # Get goal status
        daily_status, _ = DailyGoalStatus.objects.get_or_create(
            goal=goal,
            user_data=daily_data,
        )

        if daily_status.completed:
            # Exit out early, don't give rewards for an already completed task
            return daily_status

        # Mark as completed
        daily_status.completed = True
        daily_status.save()

        # Add xp and point reward to user
        user.xp += goal.xp_reward
        user.points += goal.point_reward

        user.save()

        # Finding if need to add streak and adding or resetting
        daily_goals = DailyGoalStatus.objects.filter(
            user_data__user=user, completed=True)

        # If havent added streak today and have complted at least one goal
        today = datetime.datetime.combine(
            datetime.date.today(),
            datetime.time(0, 0)
        )

        # Check for specific personal goal
        if goal.type == Goal.PERSONAL and "Water" in goal.name:
            Statistics.increment_quantity("water")
        if goal.type == Goal.PERSONAL and "Recycle" in goal.name:
            Statistics.increment_quantity("plastic")

        # Django treats DateFields weirdly
        # Occasionally it returns a date object instead of datetime
        # This handles that edge case
        last_completed = user.date_last_task_completed
        if isinstance(last_completed, datetime.date):
            last_completed = datetime.datetime.combine(
                last_completed,
                datetime.time(0, 0)
            )

        if (today - datetime.timedelta(days=1) > last_completed):
            user.streak_length = 0
            user.date_last_task_completed = today
            user.save()
        elif ((last_completed < today) and len(daily_goals) > 0):
            user.streak_length += 1
            user.date_last_task_completed = today
            user.save()
        
        return daily_status

class DailyGoalStatus(models.Model):
    """
    A representation of a goal for a specific user
    Whenever a user attempts a goal one of these objects is created for said user
    A relation model between a user data and a goal
    """
    user_data = models.ForeignKey(DailyData, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    score = models.IntegerField(default=0)

    def xp_reward(self):
        return self.goal.xp_reward or 0

    def point_reward(self):
        return self.goal.point_reward or 0
