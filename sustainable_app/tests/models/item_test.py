from django.test import TestCase

from ...models import Item


class ItemModelTests(TestCase):
    def test_str(self):
        """
        Checks the __str__ function returns name
        """
        item = Item(name="test-name")

        self.assertIs(str(item), item.name)
