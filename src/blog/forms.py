from django import forms
from .models import Blog, BlogComment


class BlogForm(forms.ModelForm):
    """Respresenting Blog Form"""
    class Meta:
        model = Blog
        fields = ('title', 'thumbnail', 'content')

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].required = False


class CommentForm(forms.ModelForm):
    """Respresenting comment form"""
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
            'rows': 4
        }))
    class Meta:
        model  = BlogComment
        fields = ('content',)
