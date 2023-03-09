from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
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
    
    clue = models.CharField(max_length=200)
    image = models.ImageField(upload_to='location_images', height_field=None, width_field=None, max_length=100)
    qr = models.ImageField(upload_to='location_qr', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name
