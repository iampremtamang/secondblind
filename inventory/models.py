from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True) #Just overriding for the sake of requirement
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True, db_index=True)

    def __str__(self):
        return self.title
