from django.test import TestCase

from ...models import Statistics


class StatisticsModelTests(TestCase):
    def test_increment_quantity_once(self):
        """
        Checks the increment_quantity function increments the quantity
        attribute once
        """

        Statistics.objects.create(name="test", quantity=0)

        Statistics.increment_quantity("test")

        statistic = Statistics.objects.get(name="test")
        self.assertEqual(statistic.quantity, 1)

    def test_increment_quantity_many(self):
        """
        Checks the increment_quantity function increments the quantity
        attribute for many runs
        """

        Statistics.objects.create(name="test", quantity=0)

        for _ in range(100):
            Statistics.increment_quantity("test")

        statistic = Statistics.objects.get(name="test")
        self.assertEqual(statistic.quantity, 100)
