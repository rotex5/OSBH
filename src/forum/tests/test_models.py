from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Forum

class ForumModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='testuser', password='testpass')
        test_user.save()
        Forum.objects.create(topic='Test Forum', content='This is a test forum', creator=test_user)

    def test_topic_max_length(self):
        # Test to make sure the topics max length is less than or 1000
        forum = Forum.objects.get(id=1)
        max_length = forum.__meta.get_field('topic').max_length
        self.assertEquals(max_length, 1000)

    def test_content_max_length(self):
        # Test to make sure the contents length is less than or 2000
        forum = Forum.objects.get(id=1)
        max_length = forum.__meta.get_field('content').max_length
        self.assertEquals(max_length, 2000)

    def test_get_absolute_url(self):
        # 
        forum = Forum.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(forum.get_absolute_url(), '/forums/1')

    def test_topic_string_representation(self):
        forum = Forum.objects.get(id=1)
        self.assertEquals(str(forum), 'Test Forum')

    def test_topic_string_representation_long_topic(self):
        forum = Forum.objects.get(id=1)
        forum.topic = 'This is a very long topic that should be truncated by the __str__ method.'
        forum.save()
        self.assertEquals(str(forum), 'This is a very long topic that should be trunca...')

    def test_creator_null(self):
        forum = Forum.objects.create(topic='Test Forum 2')
        self.assertIsNone(forum.creator)

    def test_creator_not_null(self):
        test_user = User.objects.get(username='testuser')
        forum = Forum.objects.create(topic='Test Forum 3', creator=test_user)
        self.assertEquals(forum.creator, test_user)