from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=500)
    rating = models.IntegerField()
    author = models.CharField(max_length=50)