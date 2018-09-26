from django.db import models


class Location(models.Model):
    """
    Class that contains location details of the image posted
    """
    name = models.CharField(max_length = 15)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def del_location(self):
        self.delete()


class Category(models.Model):
    """
    Class that contains the category details of the image posted
    """
    name = models.CharField(max_length = 15)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save_cat(self):
        self.save()

    def del_cat(self):
        self.delete()



class Image(models.Model):
    """
    Class that contains details concerning the image itself
    """
    photo = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 25)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    # up_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

