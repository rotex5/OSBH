from django.test import TestCase
from django.contrib.auth.models import User
from forum.models import Thread, Discussion


class ThreadModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='testuser')

        Thread.objects.create(
            title='Test Thread', content='This is a test thread.',
            author=user)

    def test_title_max_length(self):
        thread = Thread.objects.get(id=1)
        max_length = thread._meta.get_field('title').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_is_title(self):
        thread = Thread.objects.get(id=1)
        expected_object_name = thread.title
        self.assertEquals(expected_object_name, str(thread))

    def test_get_absolute_url(self):
        thread = Thread.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(thread.get_absolute_url(), '/threads/1/')


class DiscussionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='testuser')

        thread = Thread.objects.create(
            title='Test Thread', content='This is a test thread.',
            author=user)

        Discussion.objects.create(
            thread=thread, content='This is a test discussion.',
            author=user)

    def test_object_name_is_content(self):
        discussion = Discussion.objects.get(id=1)
        expected_object_name = discussion.content
        self.assertEquals(expected_object_name, str(discussion))

    def test_comment_max_length(self):
        discussion = Discussion.objects.get(id=1)
        max_length = discussion._meta.get_field('content').max_length
        self.assertEquals(max_length, 1000)

