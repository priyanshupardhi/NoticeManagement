from django.db import models
from django.utils import timezone

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(default=timezone.now)
