"""
Description of Models in the Posts app
"""

from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import User

# Create your models here.

CHOICES = [
    ("ebook", "Ebook"),
    ("video", "Video"),
    ("music", "Music"),
    ("image", "Image"),
    ("other", "Other"),
]


class Post(models.Model):
    """
    Post model store information about posts.
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_file = models.FileField(upload_to="uploads/")
    thumbnail_image = models.ImageField(
        default="default.jpg", upload_to="thumbnail_images"
    )
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, choices=CHOICES, default="other")
    is_private = models.BooleanField(default=False)

    def get_absolute_url(self):
        """
        Generates and returns url to a particular post model instance
        """
        return reverse("Posts-detail", kwargs={"pk": self.pk})

    def __str__(self):
        """
        funtion returns the title of particular instance of Post object

        Return:
            it returns the title of particular instance of Post object
        """
        return f"{self.title}"


class Comment(models.Model):
    """
    Comment model stores information regarding comments under the posts
    """

    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date_time = models.DateTimeField(editable=False, default=timezone.now)
