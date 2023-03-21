from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from forum.models import Forum, Discussion
from forum.forms import ForumForm
import json

class ForumViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.forum = Forum.objects.create(
            topic='Test Forum',
            description='This is a test forum',
            creator=self.user
        )
        self.discussion = Discussion.objects.create(
            forum=self.forum,
            message='This is a test message',
            commenter=self.user
        )

    def test_list_forum_view(self):
        response = self.client.get(reverse('forums'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum-list.html')
        self.assertContains(response, 'Test Forum')

    def test_forum_create_view(self):
        self.client.login(username='testuser', password='testpass')
        form_data = {
            'topic': 'New Forum',
            'description': 'This is a new test forum'
        }
        response = self.client.post(reverse('forum-create'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Forum.objects.count(), 2)
        new_forum = Forum.objects.get(topic='New Forum')
        self.assertEqual(new_forum.creator, self.user)
        self.assertRedirects(response, reverse('forum-detail', kwargs={'id': new_forum.id}))

    def test_forum_detail_view(self):
        response = self.client.get(reverse('forum-detail', kwargs={'id': self.forum.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum-detail.html')
        self.assertContains(response, 'Test Forum')
        self.assertContains(response, 'This is a test message')

    def test_getMessages_view(self):
        response = self.client.get(reverse('getMessages', kwargs={'id': self.forum.id}))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['messages']), 1)
        self.assertEqual(data['messages'][0]['forum'], self.forum.id)
        self.assertEqual(data['messages'][0]['message'], 'This is a test message')
        self.assertEqual(data['messages'][0]['commenter__username'], 'testuser')

    def test_send_view(self):
        self.client.login(username='testuser', password='testpass')
        form_data = {'message': 'This is a new test message'}
        response = self.client.post(reverse('send', kwargs={'id': self.forum.id}), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Discussion.objects.count(), 2)
        new_message = Discussion.objects.last()
        self.assertEqual(new_message.forum, self.forum)
        self.assertEqual(new_message.message, 'This is a new test message')
        self.assertEqual(new_message.commenter, self.user)

    def test_forum_delete_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('forum-delete', kwargs={'id': self.forum.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Forum.objects.count(), 0)

