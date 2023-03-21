from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Blog, BlogAuthor, BlogView, BlogLike


class BlogViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.author = BlogAuthor.objects.create(
            user=self.user,
            bio='This is a test bio.'
        )
        self.blog = Blog.objects.create(
            title='Test blog',
            content='This is a test blog.',
            author=self.author
        )

    def test_list_blog_view(self):
        url = reverse('blog-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.blog.title)

    def test_blog_create_view(self):
        url = reverse('blog-create')
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url, {'title': 'New test blog', 'content': 'This is a new test blog.'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), 2)

    def test_blog_detail_view(self):
        url = reverse('blog-detail', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.blog.title)
        self.assertContains(response, self.blog.content)

    def test_blog_update_view(self):
        url = reverse('blog-update', args=[self.blog.id])
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url, {'title': 'Updated test blog', 'content': 'This is an updated test blog.'})
        self.assertEqual(response.status_code, 302)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, 'Updated test blog')
        self.assertEqual(self.blog.content, 'This is an updated test blog.')

    def test_blog_delete_view(self):
        url = reverse('blog-delete', args=[self.blog.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), 0)

    def test_author_detail_view(self):
        url = reverse('author-detail', args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.bio)

    def test_blog_like_view(self):
        url = reverse('blog-like', args=[self.blog.id])
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogLike.objects.count(), 1)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogLike.objects.count(), 0)

