from django import forms
from .models import Thread, Discussion


class ThreadForm(forms.ModelForm):
    """Respresenting Thread Form"""
    class Meta:
        model = Thread
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False


class DiscussionForm(forms.ModelForm):
    """Respresenting a Discussion Form"""
    class Meta:
        model = Discussion
        fields = ('content',)
