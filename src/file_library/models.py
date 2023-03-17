from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


# Create your models here.
class FileUploader(models.Model):
    """
    Model representing a file uploader.
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    has_uploaded = models.BooleanField(default=False)

    class Meta:
        ordering = ["user", "has_uploaded"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username


class File(models.Model):
    """Model representing a file"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='files/pdfs/')
    cover = models.ImageField(upload_to='files/covers/', null=True,
                              blank=True, default='files/covers/default.jpg')
    uploader = models.ForeignKey(
        FileUploader, on_delete=models.SET_NULL, null=True, blank=True)
    PICK_CATEGORY = (
        ('A', 'Art'),
        ('AE', 'Academic & Education'),
        ('B', 'Biography'),
        ('BC', 'Business & Career'),
        ('E', 'Environment'),
        ('FL', 'Fiction & Literature'),
        ('HF', 'Health & Fitness'),
        ('LS', 'Lifestyle'),
        ('PG', 'Personal Growth'),
        ('PL', 'Politics & Laws'),
        ('R', 'Religion'),
        ('SR', 'Science & Research'),
        ('T', 'Technology'),
    )
    category = models.CharField(
        max_length=2, choices=PICK_CATEGORY, blank=True, default='AE')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Returns the url to access a particular file instance."""
        return reverse('file-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    """ When any user instance created, FileUploader object
    instance is created and automatically linked by User """
    if created:
        FileUploader.objects.create(user=instance)
    else:
        instance.fileuploader.save()
