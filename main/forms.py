from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Post, Comment, User

class CreatePostForm(forms.ModelForm):
  image = forms.ImageField(required=False)
  class Meta:
    model = Post
    fields = ['content', 'image']


class CreateCommentForm(forms.ModelForm):
  def __init__(self, post, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.post = post
      
  class Meta:
    model = Comment
    fields = ('content',)


class CustomUserCreationForm(UserCreationForm):
  avatar = forms.ImageField(required=False)
  bio = forms.CharField(max_length=500, required=False)

  class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)
