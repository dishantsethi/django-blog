from django.db import models
from django.utils import timezone
from datetime import datetime    


# Create your models here.
class articles(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
