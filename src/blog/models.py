from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class BlogAuthor(models.Model):
    """
    Model representing a blog author.
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    class Meta:
        ordering = ["user", "bio"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username


class BlogComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title = 70
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring
