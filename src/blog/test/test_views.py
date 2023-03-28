from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Blog, BlogAuthor, BlogView, BlogLike


class BlogViewsTestCase(TestCase):
    print("setUp method is being called")
    def setup(self):
        self.client = Client()
		"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )
        self.blog = Blog.objects.create(
            title='test blog',
            content='This is a test blog',
            author=self.user
        )
    """
    def test_list_blog_view(self):
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
        url = reverse('blogs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.blog.title)

    def test_blog_create_view(self):
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

        url = reverse('blog-create')
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url, {'title': 'New test blog', 'content': 'This is a new test blog.'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), 2)

    def test_blog_detail_view(self):
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

        url = reverse('blog-detail', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.asserContains(response, self.blog.title)
        self.assertContains(response, self.blog.content)

    def test_blog_update_view(self):
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

        url = reverse('blog-update', args=[self.blog.id])
        self.clent.login(username='testuser', password='testpass')
        response = self.client.post(url, {'title': 'Updated test blog', 'content': 'This is an updated version of the previous created blog.'})
        self.assertEqual(response.status_code, 302)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, 'Updated test blog')
        self.assertEqual(self.blog.content, 'This is an updated version of the previous created blog.')
        self.assertEqual(Blog.objects.count(), 2)

    def test_blog_delete_view(self):
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

        url = reverse('blog-delete', args=[self.blog.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), 0)

    def test_author_detail_view(self):
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

        url = reverse('author-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertContains(response, self.user.bio)

    def test_blog_like_view(self):
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

        url = reverse('blog-like', args=[self.blog.id])
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogLike.objects.count(), 0)
