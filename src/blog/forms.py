from django import forms
from .models import BlogComment 


class CommentForm(forms.ModelForm):
    """Respresenting comment form"""
    class Meta:
        model  = BlogComment
        fields = ('description',)
