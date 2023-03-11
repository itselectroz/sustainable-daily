from django.test import TestCase

from ...models import Location


class LocationModelTests(TestCase):
    def test_str(self):
        """
        Checks the __str__ function returns name
        """
        location = Location(name="test-name")

        self.assertIs(str(location), location.name)
        
    def test_path_and_rename(self):
        """
        Checks the path_and_rename function returns the correct path
        """
        location = Location(name="test-name")
        
        self.assertIs(location.image.upload_to == "location/img" + str(location.id))
