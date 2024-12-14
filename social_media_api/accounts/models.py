from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


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
    followers = models.ManyToManyField('self', symmetrical=False, related_name='is_followed_by', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='is_following', blank=True)

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
    
    def follow_user(self, user):
        """Follow another user."""
        self.following.add(user)
    
    def unfollow_user(self, user):
        """
        Unfollow another user
        """
        self.following.remove(user)
    
    def is_following(self, user):
        """
        
        """
        return self.following.filter(id=user.id).exists()
    
    def is_followed_by(self, user):
        """
        Check if the current user is followed by another users.
        """
        return self.following.filter(id=user.id).exixts()
    
    
