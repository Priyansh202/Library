from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title
