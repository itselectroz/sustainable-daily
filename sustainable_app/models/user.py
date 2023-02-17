import math

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200) # change max length for these
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    # Password stuff
    password = models.CharField(max_length=200)
    salt = models.CharField(max_length=200)

    # Account stuff
    xp = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    
    weekly_xp = models.IntegerField(default=0) # gets reset every monday


    # owned_items = models.ManyToManyField(Item)
    # equipped_items = models.ManyToManyField(Item)
    
    # Personal goals is a relation that will be in goal maybe?

    ### Methods

    def username(self):
        return f"{self.first_name} {self.last_name}"
    
    def level(self):
        return math.floor(0.07 * math.sqrt(self.xp))
    
    def xp_for_level(self, level):
        return math.floor((level / 0.07) ** 2)
