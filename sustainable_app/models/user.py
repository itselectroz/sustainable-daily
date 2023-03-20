import math

from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import date

from .item import Item


class User(AbstractUser):
    # Account stuff
    xp = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    game_keeper = models.BooleanField(default=False)

    weekly_xp = models.IntegerField(default=0)  # gets reset every monday

    owned_items = models.ManyToManyField(Item, related_name="owned_by")
    equipped_items = models.ManyToManyField(Item, related_name="equipped_by")

    # Streak stuff, incremented in daily data when task is complete
    streak_length = models.IntegerField(default=0)
    date_last_task_completed = models.DateTimeField(default=date.today)

    # Personal goals is a relation that will be in goal maybe?

    # Methods

    def level(self):
        return math.floor(0.07 * math.sqrt(self.xp))

    def xp_for_level(self, level):
        return math.floor((level / 0.07) ** 2)
