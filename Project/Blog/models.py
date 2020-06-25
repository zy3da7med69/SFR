from django.db import models

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=100)
    Email = models.EmailField()
    Content = models.TextField(max_length=1000)
