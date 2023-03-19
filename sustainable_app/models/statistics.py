from django.db import models

class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    # Either plastic bottles saved or items recycled
    quantity = models.IntegerField()