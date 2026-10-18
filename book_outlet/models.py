from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=500)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(max_length=50)
    is_bestselling = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2,default=100.00)

    def get_absolute_url(self):
        return f"/book_outlet/{self.id}/"
    
    def __str__(self):
        return f"{self.title} by {self.author} - {self.rating}/5 {'(Bestselling)' if self.is_bestselling else '(Not Bestselling)'}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"


