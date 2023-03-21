from django.test import TestCase
from .forms import ForumForm
from .models import Forum

class ForumFormTest(TestCase):
    def test_forum_form_fields(self):
        form = ForumForm()
        self.assertTrue('topic' in form.fields)
        self.assertTrue('content' in form.fields)

    def test_forum_form_content_field_not_required(self):
        form = ForumForm()
        self.assertFalse(form.fields['content'].required)

    def test_forum_form_with_valid_data(self):
        form_data = {
            'topic': 'Test Topic',
            'content': 'Test content',
        }
        form = ForumForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forum_form_with_empty_data(self):
        form = ForumForm(data={})
        self.assertFalse(form.is_valid())
        self.assertTrue('topic' in form.errors)

