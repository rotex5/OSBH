from django.test import TestCase
from blog.forms import BlogForm, CommentForm
from blog.models import Blog, BlogComment

class BlogFormTest(TestCase):
    def test_blog_form_fields(self):
        form = BlogForm()
        self.assertTrue('title' in form.fields)
        self.assertTrue('thumbnail' in form.fields)
        self.assertTrue('content' in form.fields)

    def test_blog_form_thumbnail_not_required(self):
        form = BlogForm()
        self.assertFalse(form.fields['thumbnail'].required)

    def test_blog_form_with_valid_data(self):
        form_data = {
            'title': 'Test Title',
            'content': 'Test content',
        }
        form = BlogForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blog_form_with_empty_data(self):
        form = BlogForm(data={})
        self.assertFalse(form.is_valid())
        self.assertTrue('title' in form.errors)

class CommentFormTest(TestCase):
    def test_comment_form_fields(self):
        form = CommentForm()
        self.assertTrue('content' in form.fields)

    def test_comment_form_with_valid_data(self):
        form_data = {
            'content': 'Test comment',
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_with_empty_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertTrue('content' in form.errors)
