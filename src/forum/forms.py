from django import forms
from .models import Forum 


class ForumForm(forms.ModelForm):
    """Respresenting Forum Form"""
    class Meta:
        model = Forum
        fields = ('topic', 'content', )

    def __init__(self, *args, **kwargs):
        super(ForumForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False
