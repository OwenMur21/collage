from django.test import TestCase
from .models import Location, Category, Image

class LocationTestClass(TestCase):
    """
    Tests Location class and its functions
    """
    #Set up method
    def setUp(self):
        self.locale = Location(name='here', description='testing pic')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.locale, Location))
    
    def test_save_method(self):
        """
        Function to test that location is being saved
        """
        self.locale.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        """
        Function to test that a location can be deleted
        """
        self.locale.save_location()
        self.locale.del_location()
    
    def test_update_method(self):
        """
        Function to test that a location's details can be updates
        """
        self.locale.save_location()
        new_place = Location.objects.filter(name='here').update(name='hapa')
        locations = Location.objects.get(name='hapa')
        self.assertTrue(locations.name, 'hapa')

class CategoryTestClass(TestCase):
    """
    Tests category class and its functions
    """
    #Set up method
    def setUp(self):
        self.cat = Category(name='this', description='testing pic')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))
    
    def test_save_method(self):
        """
        Function to test that category is being saved
        """
        self.cat.save_cat()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        """
        Function to test that a category can be deleted
        """
        self.cat.save_cat()
        self.cat.del_cat()
    
    def test_update_method(self):
        """
        Function to test that a category's details can be updates
        """
        self.cat.save_cat()
        new_cat = Category.objects.filter(name='this').update(name='hii')
        categories = Category.objects.get(name='hii')
        self.assertTrue(categories.name, 'hii')



class ImageTestClass(TestCase):
    """
    Tests Image class and its functions
    """
    #Set up method
    def setUp(self):
        self.image = Image(photo='test.jpg', name='testing pic', description='test times at testcase', location='here', category='tests')

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


