from django.test import TestCase
from .forms import FileForm
from .models import File

class FileFormTestCase(TestCase):

    def test_valid_form(self):
        file_data = {
            'title': 'Test Title',
            'author': 'Test Author',
            'category': 'Test Category',
            'pdf': 'test.pdf',
            'cover': 'test.jpg'
        }
        form = FileForm(data=file_data)
        self.assertTrue(form.is_valid())

    def test_blank_form(self):
        form = FileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

