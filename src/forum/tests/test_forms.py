from django.test import TestCase
from forum.forms import ThreadForm, DiscussionForm
from forum.models import Thread, Discussion


class ThreadFormTest(TestCase):
    def test_valid_form(self):
        data = {'title': 'Test Thread', 'content': 'This is a test thread.'}
        form = ThreadForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': '', 'content': ''}
        form = ThreadForm(data=data)
        self.assertFalse(form.is_valid())

    def test_content_not_required(self):
        form = ThreadForm()
        self.assertFalse(form.fields['content'].required)


class DiscussionFormTest(TestCase):
    def test_valid_form(self):
        data = {'content': 'This is a test discussion.'}
        form = DiscussionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'content': ''}
        form = DiscussionForm(data=data)
        self.assertFalse(form.is_valid())

