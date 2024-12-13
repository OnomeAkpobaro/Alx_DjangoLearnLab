from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Create new user
        """
        if not email:
            raise ValueError("Enter a valid email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        Creats a superuser
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class AccountUser(AbstractUser):
    """
    Extended user model, adds additional fields for social media profile
    """
    email = models.EmailField(unique=True, max_length=255)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(('profile picture'), upload_to = 'proflie_pics/', blank=True, null=True),
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username
    
    def get_followers_count(self):
        """
        Returns the total number of followers
        """
        return self.followers.count()
    
    def get_following_count(self):
        """
        Returns the total number of users followed by this user
        """
        return self.following.count()
    
