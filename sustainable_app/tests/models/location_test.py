from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

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
        
        location = Location(name="test-name", category="test-category", clue="test-clue")
        location.save()

        # test input file
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        location.image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
        location.save()
        
        self.assertEquals(location.image.url, "/location_images/img_" + str(location.id) + ".png")
        
        location.image.delete(save=False)

        
