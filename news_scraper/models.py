from django.conf import settings
from django.db import models
from django.utils import timezone

class News(models.Model):
    image_url= models.URLField()
    title = models.CharField(max_length=200)
    lead = models.CharField(max_length=200)
    body = models.TextField()
    time = models.DateTimeField()
    time_txt = models.CharField(max_length=100)

def __str__(self):
    return self.title




