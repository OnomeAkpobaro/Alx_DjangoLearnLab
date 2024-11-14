from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.conf import settings
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_picture/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        user= self.create_user(username, email, password, date_of_birth, profile_photo)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
