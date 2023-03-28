from django.test import Client, TestCase
from django.urls import reverse
from django.core import mail
from file_library.models import File
from file_library.views import file_list

class FileListTest(TestCase):
    def setUp(self):
		self.client = Client()
        self.url = reverse('file-list')
        self.file = File.objects.create(title='Test File', description='Test Description')

    def test_file_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'file_library/file_list.html')
        self.assertIn(self.file, response.context['files'])

    def test_file_list_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_file_list_context(self):
        response = self.client.get(self.url)
        self.assertQuerysetEqual(response.context['files'], [repr(self.file)])
    def test_file_list_pagination(self):
        for i in range(10):
            File.objects.create(title=f'Test File {i}', description=f'Test Description {i}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'file_library/file_list.html')
        self.assertEqual(len(response.context['files']), 5)
        self.assertTrue(response.context['files'].has_previous())
        self.assertTrue(response.context['files'].has_next())
    
    def test_search_result_view(self):
        response = self.client.post(reverse('search-result'), {'searched': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search-result.html')
        self.assertIn(self.file, response.context['file_results'])
    
    def test_contact_us_view(self):
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email_address': 'test@example.com',
            'message': 'This is a test message'
        }
        response = self.client.post(reverse('contact-us'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Website Inquiry')
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
