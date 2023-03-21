from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import File, FileUploader
from .forms import FileForm
from blog.models import Blog


class FileListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('file-list')
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass')
        self.file = File.objects.create(
            title='Test File',
            author='Test Author',
            pdf=SimpleUploadedFile("file.pdf", b"file_content"),
            uploader=FileUploader.objects.create(user=self.user)
        )

    def test_file_list_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_file_list_context(self):
        response = self.client.get(self.url)
        self.assertQuerysetEqual(response.context['files'], [repr(self.file)])


class FileDetailTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass')
        self.file = File.objects.create(
            title='Test File',
            author='Test Author',
            pdf=SimpleUploadedFile("file.pdf", b"file_content"),
            uploader=FileUploader.objects.create(user=self.user)
        )
        self.url = reverse('file-detail', args=[self.file.id])

    def test_file_detail_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_file_detail_context(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['file'], self.file)


class FileUploadTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('file-upload')
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass')

    def test_file_upload_status_code_with_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_file_upload_status_code_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_file_upload_with_valid_data(self):
        self.client.login(username='testuser', password='testpass')
        pdf = SimpleUploadedFile("file.pdf", b"file_content")
        form_data = {
            'title': 'New Test File',
            'author': 'New Test Author',
            'pdf': pdf,
        }
        form = FileForm(data=form_data, files={'pdf': pdf})
        response = self.client.post(self.url, data=form_data, files={'pdf': pdf})
        self.assertTrue(File.objects.filter(title='New Test File').exists())

    def test_file_upload_with_invalid_data(self):
        self.client.login(username='testuser', password='testpass')
        form_data = {
            'title': '',
            'author': '',
            'pdf': '',
        }
        form = FileForm(data=form_data, files={})
        response = self.client.post(self.url, data=form_data, files={})
        self.assertFormError(response, 'form', 'title', 'This field is required.')
        self.assertFormError(response, 'form', 'author', 'This field is required.')
        self.assertFormError(response, 'form)
