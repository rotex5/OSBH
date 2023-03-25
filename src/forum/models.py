from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Thread(models.Model):
    """
    Model representing a thread.
    """
    title = models.CharField(max_length=1000)
    content = models.TextField(max_length=2000, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        """
        Returns the url to access a particular forum instance.
        """
        return reverse('thread-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        len_title = 70
        if len(self.title) > len_title:
            titlestring = self.title[:len_title] + '...'
        else:
            titlestring = self.title
        return titlestring


class Discussion(models.Model):
    """
    Model representing a Discussion.
    """
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        len_comment = 70
        if len(self.content) > len_comment:
            commentstring = self.content[:len_comment] + '...'
        else:
            commentstring = self.content
        return commentstring
