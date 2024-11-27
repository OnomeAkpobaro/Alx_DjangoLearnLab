from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an author with a name.
    """
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with title, publication year and author.
    """
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    