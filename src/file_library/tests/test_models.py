from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from file_library.models import FileUploader, File

class FileUploaderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.uploader = FileUploader.objects.create(user=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.uploader), 'testuser')

    def test_has_uploaded_default_value(self):
        self.assertFalse(self.uploader.has_uploaded)


class FileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.uploader = FileUploader.objects.create(user=self.user)
        self.file = File.objects.create(
            title='Test File',
            author='Test Author',
            pdf=SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf"),
            uploader=self.uploader
        )

    def test_string_representation(self):
        self.assertEqual(str(self.file), 'Test File')

    def test_get_absolute_url(self):
        url = reverse('file-detail', args=[str(self.file.id)])
        self.assertEqual(self.file.get_absolute_url(), url)

    def test_category_choices(self):
        choices = ('A', 'AE', 'B', 'BC', 'E', 'FL', 'HF', 'LS', 'PG', 'PL', 'R', 'SR', 'T')
        for choice in choices:
            self.assertIn(choice, dict(self.file.PICK_CATEGORY).keys())

    def test_uploaded_at_auto_now_add(self):
        self.assertIsNotNone(self.file.uploaded_at)

    def test_file_upload(self):
        self.assertEqual(self.file.pdf.name, 'files/pdfs/file.pdf')
        self.assertEqual(self.file.cover.name, None)

    def test_uploader_can_be_null(self):
        file = File.objects.create(
            title='Test File 2',
            author='Test Author',
            pdf=SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf"),
        )
        self.assertEqual(file.uploader, None)
