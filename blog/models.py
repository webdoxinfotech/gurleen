from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(default='images/default.jpg', upload_to='images/')
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
