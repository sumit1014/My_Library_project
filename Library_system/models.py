from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=255)
    book_num =  models.PositiveIntegerField()
    added_time =models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.book_name
