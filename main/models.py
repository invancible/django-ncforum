from django.db import models


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
  
  