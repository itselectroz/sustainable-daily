import math

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Account stuff
    xp = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    weekly_xp = models.IntegerField(default=0)  # gets reset every monday

    # owned_items = models.ManyToManyField(Item)
    # equipped_items = models.ManyToManyField(Item)

    # Personal goals is a relation that will be in goal maybe?

    # Methods

    def level(self):
        return math.floor(0.07 * math.sqrt(self.xp))

    def xp_for_level(self, level):
        return math.floor((level / 0.07) ** 2)
