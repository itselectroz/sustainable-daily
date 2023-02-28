from django.db import models


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    cost = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name
