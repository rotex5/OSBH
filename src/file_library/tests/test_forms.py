from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from filelibrary.models import File
from filelibrary.forms import FileForm, ContactForm


class FileFormTestCase(TestCase):
    def setUp(self):
        self.valid_file_data = {
            'title': 'Test File',
            'author': 'Test Author',
            'category': 'Test Category',
            'pdf': SimpleUploadedFile('test.pdf', b'file_content'),
            'cover': SimpleUploadedFile('test.png', b'file_content'),
        }
        self.invalid_file_data = {
            'title': '',
            'author': '',
            'category': '',
            'pdf': SimpleUploadedFile('test.pdf', b'file_content'),
            'cover': SimpleUploadedFile('test.png', b'file_content'),
        }

    def test_valid_form(self):
        form = FileForm(data=self.valid_file_data)
        self.assertTrue(form.is_valid())

	def test_blank_form(self):
        form = FileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

    def test_invalid_form(self):
        form = FileForm(data=self.invalid_file_data)
        self.assertFalse(form.is_valid())

    def test_missing_required_fields(self):
        form = FileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('author', form.errors)
        self.assertIn('category', form.errors)

    def test_max_length_validation(self):
        long_title = 'a' * 101
        long_author = 'a' * 51
        long_category = 'a' * 51
        invalid_data = {
            'title': long_title,
            'author': long_author,
            'category': long_category,
            'pdf': SimpleUploadedFile('test.pdf', b'file_content'),
            'cover': SimpleUploadedFile('test.png', b'file_content'),
        }
        form = FileForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('author', form.errors)
        self.assertIn('category', form.errors)

    def test_file_upload_validation(self):
        invalid_data = {
            'title': 'Test File',
            'author': 'Test Author',
            'category': 'Test Category',
            'pdf': SimpleUploadedFile('test.txt', b'file_content'),
            'cover': SimpleUploadedFile('test.txt', b'file_content'),
        }
        form = FileForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('pdf', form.errors)
        self.assertIn('cover', form.errors)


class ContactFormTestCase(TestCase):
    def setUp(self):
        self.valid_contact_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email_address': 'john.doe@example.com',
            'message': 'Test message',
        }
        self.invalid_contact_data = {
            'first_name': '',
            'last_name': '',
            'email_address': '',
            'message': '',
        }

    def test_valid_ContactForm(self):
        form = ContactForm(data=self.valid_contact_data)
        self.assertTrue(form.is_valid())

    def test_invalid_ContactForm(self):
        form = ContactForm(data=self.invalid_contact_data)
        self.assertFalse(form.is_valid())

    def test_max_length_validation(self):
        long_first_name = 'a' * 51
        long_last_name = 'a' * 51
        long_email_address = 'a' * 151
        long_message = 'a' * 2001
        invalid_data = {
            'first_name': long_first_name,
            'last_name': long_last_name,
            'email_address': long_email_address,
		}

