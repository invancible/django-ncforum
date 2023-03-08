from django import forms

from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'


class CreateCommentForm(forms.ModelForm):
  def __init__(self, post, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.post = post
      
  class Meta:
    model = Comment
    fields = ('content',)

