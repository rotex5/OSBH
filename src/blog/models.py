from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from ckeditor.fields import RichTextField


class Blog(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    content = RichTextField(null=True, blank=True,
                            config_name="special", external_plugin_resources=[(
                                'youtube', '/static/shareledge/ckeditor-plugins/youtube/youtube/', 'plugin.js',
                            )])
    thumbnail = models.ImageField(
        upload_to='blogs/thumbnails/', null=True, blank=True)
    author = models.ForeignKey(
        'BlogAuthor', on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish_date"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_like_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog-like', args=[str(self.id)])

    @property
    def get_comment_count(self):
        return self.blogcomment_set.all().count()

    @property
    def get_view_count(self):
        return self.blogview_set.all().count()

    @property
    def get_like_count(self):
        return self.bloglike_set.all().count()


class BlogAuthor(models.Model):
    """
    Model representing a blog author.
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(
        max_length=400, help_text="Enter your bio details here.")

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
    content = models.TextField(
        max_length=1000, help_text="Enter comment about blog here.")
    commenter = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title = 70
        if len(self.content) > len_title:
            titlestring = self.content[:len_title] + '...'
        else:
            titlestring = self.content
        return titlestring


class BlogView(models.Model):
    """
    No of view associated with a blog
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class BlogLike(models.Model):
    """
    Like assocated with a blog
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    """ When any user instance created, FileUploader object
    instance is created and automatically linked by User """
    if created:
        BlogAuthor.objects.create(user=instance)
    else:
        instance.blogauthor.save()
