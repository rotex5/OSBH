from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from mixer.backend.django import mixer
from forum.models import Thread
from forum.forms import DiscussionForm, ThreadForm
from forum.views import list_thread, thread_detail, thread_create


class ForumViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.thread = mixer.blend(Thread, author=self.user)

    def test_list_thread_view(self):
        url = reverse('forum')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread-list.html')

    def test_thread_detail_view(self):
        url = reverse('thread-detail', args=[self.thread.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread-detail.html')

    def test_thread_create_view(self):
        url = reverse('thread-create')
        #url = '/forum/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread-create.html')
        
        data = {
            'Title': 'Test Title',
            'Content': 'Test Content'
        }
        response = self.client.post(url, data)
        #print(response.status_code)
        #print(response.content)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Thread.objects.count(), 1)

