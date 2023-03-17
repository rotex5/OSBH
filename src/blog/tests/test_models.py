from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import BlogAuthor, Blog, BlogComment, BlogView, BlogLike
import sys
from django.db.models.signals import post_save
from django.dispatch import receiver

class BlogAuthorModelTest(TestCase):

    sys.stdout.write('Test')


    @classmethod
    def setupTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        #BlogAuthor.objects.create(user=test_user1, bio='Funfact: Im the second blog author')

    @classmethod
    @receiver(post_save, sender = User)
    def user_is_created(sender, instance, created, **kwargs):
        """ When any user instance created, FileUploader object
        instance is created and automatically linked by User """
        if created:
            BlogAuthor.objects.create(user=instance)
        else:
            instance.blogauthor.save()

    def test_get_absolute_url(self):
        author=BlogAuthor.objects.get(id=3)
        self.assertEquals(author.get_absolute_url(), '/blog/author/3')
