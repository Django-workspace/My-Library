from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=250)


    def __str__(self):
        return self.title

# Create your models here.
