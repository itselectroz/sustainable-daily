from django.db import models
from django.utils.html import mark_safe
import os


class Location(models.Model):
    
    # attributes
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    RECYCLE = "recycle"
    WATER = "water"
    
    category = models.CharField(
        max_length = 7,
        choices = [
            (RECYCLE, "Recycling Bin"),
            (WATER, "Water Fountain"),
        ]
    )
    
    # rename image file from user
    def path_and_rename(instance, filename):
        upload_to = 'location_images'
        # set filename to img_[id].png
        filename = ('img_' + str(instance.id) + '.png')
        # return the whole path to the file
        return os.path.join(upload_to, filename)
    
    clue = models.CharField(max_length=200)
    image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None, max_length=100)
    qr = models.ImageField(upload_to='location_qr', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name
    