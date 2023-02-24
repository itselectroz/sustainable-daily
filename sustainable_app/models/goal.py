from django.db import models


class Goal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    MINIGAME = "minigame"
    LOCATION = "location"
    POLL = "poll"
    PERSONAL = "personal"

    type = models.CharField(
        max_length=8,
        choices = [
            (MINIGAME, "Minigame"),
            (LOCATION, "Location"),
            (POLL, "Poll"),
            (PERSONAL, "Personal"),   
        ]
    )

    point_reward = models.IntegerField(default=0)
    xp_reward = models.IntegerField(default=0)

    def __str__(self):
        return self.name
