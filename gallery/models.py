from django.db import models


class Location(models.Model):
    """
    Class that contains location details of the image posted
    """
    name = models.CharField(max_length = 15)
    description = models.TextField()

    def __str__(self):
        return self.name
