from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal, receiver
from blog.models import user_is_created
from blog.models import Blog, BlogAuthor, BlogComment, BlogView, BlogLike


class BlogModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        BlogAuthor.objects.filter(user=self.user).delete()
        self.author = BlogAuthor.objects.create(user=self.user, bio='test bio')
        self.blog = Blog.objects.create(title='test title', content='test content', author=self.author)

    def test_blog_str(self):
        self.assertEqual(str(self.blog), 'test title')

    def test_blog_absolute_url(self):
        url = reverse('blog-detail', args=[str(self.blog.id)])
        self.assertEqual(self.blog.get_absolute_url(), url)

    def test_blog_like_url(self):
        url = reverse('blog-like', args=[str(self.blog.id)])
        self.assertEqual(self.blog.get_like_url(), url)

    def test_blog_comment_count(self):
        BlogComment.objects.create(blog=self.blog, content='test comment', commenter=self.user)
        self.assertEqual(self.blog.get_comment_count, 1)

    def test_blog_view_count(self):
        BlogView.objects.create(blog=self.blog, user=self.user)
        self.assertEqual(self.blog.get_view_count, 1)

    def test_blog_like_count(self):
        BlogLike.objects.create(post=self.blog, user=self.user)
        self.assertEqual(self.blog.get_like_count, 1)


class BlogAuthorModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        BlogAuthor.objects.filter(user=self.user).delete()
        self.author = BlogAuthor.objects.create(user=self.user, bio='test bio')

    def test_author_str(self):
        self.assertEqual(str(self.author), 'testuser')

    def test_author_absolute_url(self):
        url = reverse('author-detail', args=[str(self.author.id)])
        self.assertEqual(self.author.get_absolute_url(), url)

class BlogCommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        BlogAuthor.objects.filter(user=self.user).delete()
        self.author = BlogAuthor.objects.create(user=self.user, bio='test bio')
        self.blog = Blog.objects.create(title='test title', content='test content', author=self.author)
        self.comment = BlogComment.objects.create(blog=self.blog, content='test comment', commenter=self.user)

    def test_comment_str(self):
        self.assertEqual(str(self.comment), 'test comment')

    def test_comment_ordering(self):
        comment2 = BlogComment.objects.create(blog=self.blog, content='test comment 2', commenter=self.user)
        self.assertLess(self.comment.timestamp, comment2.timestamp)


class BlogViewModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        BlogAuthor.objects.filter(user=self.user).delete()
        self.author = BlogAuthor.objects.create(user=self.user, bio='test bio')
        self.blog = Blog.objects.create(title='test title', content='test content', author=self.author)

    def test_view_str(self):
        view = BlogView.objects.create(blog=self.blog, user=self.user)
        self.assertEqual(str(view), 'testuser')


class BlogLikeModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        BlogAuthor.objects.filter(user=self.user).delete()
        self.author = BlogAuthor.objects.create(user=self.user, bio='test bio')
        self.blog = Blog.objects.create(title='test title', content='test content', author=self.author)

    def test_like_str(self):
        like = BlogLike.objects.create(post=self.blog, user=self.user)
        self.assertEqual(str(like), 'testuser')


class SignalTestCase(TestCase):
    def test_blogauthor_created(self):
        post_save.connect(user_is_created, sender=User)

        # Verify that BlogAuthor is created automatically when User is created
        self.assertEqual(BlogAuthor.objects.count(), 0)
        user = User.objects.create(username='testuser2', password='54321')
        self.assertEqual(BlogAuthor.objects.count(), 1)

        # Verify that BlogAuthor is not created when an existing User is saved
        self.assertEqual(BlogAuthor.objects.count(), 1)
        user.save()
        self.assertEqual(BlogAuthor.objects.count(), 1)

        post_save.disconnect(user_is_created, sender=User)
