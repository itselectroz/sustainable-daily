from django.db import models

class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    
    # Either plastic bottles saved or items recycled
    quantity = models.IntegerField(default=0)

    @staticmethod
    def increment_quantity(name):
        """
        Increments the given statistic
        """

        try:
            statistic = Statistics.objects.get(name=name)
        except Statistics.DoesNotExist:
            statistic = Statistics(name=name)
            
        statistic.quantity += 1
        statistic.save()