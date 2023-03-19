from django.contrib.auth.models import User
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Forum(models.Model):
    """
    Model representing a forum.
    """
    topic = models.CharField(max_length=1000)
    content = models.TextField(max_length=2000, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        """
        Returns the url to access a particular forum instance.
        """
        return reverse('forum-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        len_topic = 70
        if len(self.topic) > len_topic:
            topicstring = self.topic[:len_topic] + '...'
        else:
            topicstring = self.topic
        return topicstring


class Discussion(models.Model):
    """
    Model representing a message.
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        len_message = 70
        if len(self.message) > len_message:
            messagestring = self.message[:len_message] + '...'
        else:
            messagestring = self.message
        return messagestring
