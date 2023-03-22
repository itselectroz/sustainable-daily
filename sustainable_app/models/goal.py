from django.db import models


class Goal(models.Model):
    """
    An object that represents a goal
    Can be a personal goal, a minigame, location, quiz or poll
    When a goal object is added to the database,
    it can appear on a users home page as one of the goals

    Requires the url field to be filled in to redirect
    to the goal so the user can complete it and
    the image field dictates what image will appear on the home page

    Can give any amount of points or xps
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    active = models.BooleanField(default=False)

    # URL of minigame and image for home page
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    MINIGAME = "minigame"
    LOCATION = "location"
    QUIZ = "quiz"
    POLL = "poll"
    PERSONAL = "personal"

    type = models.CharField(
        max_length=8,
        choices=[
            (MINIGAME, "Minigame"),
            (LOCATION, "Location"),
            (QUIZ, "Quiz"),
            (POLL, "Poll"),
            (PERSONAL, "Personal"),
        ]
    )

    point_reward = models.IntegerField(default=0)
    xp_reward = models.IntegerField(default=0)

    def __str__(self):
        return self.name
