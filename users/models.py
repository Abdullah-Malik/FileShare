"""
models.py contain information regarding the models that users app is using
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

# Create your models here.


class User(AbstractUser):
    """
    User class extends and implements the Django AbstractUser class that has all the functionality e.g. User Authentication already implemented
    """

    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        """
        funtion returns the username of particular instance of User object

        Return:
            it returns the username of particular instance of User object
        """
        return f"{AbstractUser.username} Profile"

    def save(self, *args, **kwargs):
        """
        Function is used to save the image uploaded by the user
        """
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        print(self.image.path)
        img.save(self.image.path)
