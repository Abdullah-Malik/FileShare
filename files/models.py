from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.

class FilesModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_file = models.FileField(upload_to='uploads/')
    thumbnail_image = models.ImageField(default="default.jpg", upload_to="thumbnail_images")
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

   