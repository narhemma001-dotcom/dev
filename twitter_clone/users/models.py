from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = ['email']
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    header_image = models.ImageField(upload_to='headers/', blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.user.username}'s profile"           

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        
    def save(self, *args, **kwargs):
        if self.follower.id == self.following.id:
            raise ValidationError("Can't follow yourself!")
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"