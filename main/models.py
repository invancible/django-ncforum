from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  email = models.EmailField(unique=True, null=True)
  avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
  bio = models.TextField(null=True, blank=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  def get_full_name(self):
    # Combine the first and last name fields to get the user's full name
    return f"{self.first_name} {self.last_name}"


class Post(models.Model):
  # author = 
  content = models.TextField(max_length=200)
  image = models.ImageField(upload_to='images', null=True)
  # likes = 
  # comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
  # comments = models.ManyToManyField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content[:50] 
    

class Comment(models.Model):
  # author = 
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
  content = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content
  
  