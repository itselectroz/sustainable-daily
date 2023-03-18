from django.db import models

class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    
    # Either plastic bottles saved or items recycled
    quantity = models.IntegerField(default=0)

    @staticmethod
    def increment_quantity(name):
        #TODO propper comment stuffs

        try:
            statistic = Statistics.objects.get(name=name)
        except Statistics.DoesNotExist:
            statistic = Statistics(name=name)
            
        print(statistic.quantity)
        statistic.quantity += 1
        print(statistic.quantity)
        statistic.save()