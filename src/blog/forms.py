from django import forms
from .models import Blog, BlogComment 


class BlogForm(forms.ModelForm):
    """Respresenting Blog Form"""
    class Meta:
        model = Blog
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):
    """Respresenting comment form"""
    class Meta:
        model  = BlogComment
        fields = ('description',)
