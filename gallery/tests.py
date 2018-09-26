from django.test import TestCase
from .models import Location, Category, Image


class ImageTestClass(TestCase):
    """
    Tests Image class and its functions
    """
    #Set up method
    def setUp(self):
        self.image = Image(photo='test.jpg', name='testing pic', description='test times at testcase')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        """
        Test for saving uploaded images
        """
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0 )
