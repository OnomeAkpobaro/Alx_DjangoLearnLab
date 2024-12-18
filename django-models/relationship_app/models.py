from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Book')
    class Meta:
        permissions = (
            ("can_add_book", "can add a book "),
            ("can_change_book", 'can change a book'),
            ("can_delete_book", "can delete a book")
        )
    

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class UserProfile(models.Model):
    CHOICES =(
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


