from django.test import TestCase
from django.urls import reverse
from .models import UploadedFile

class FileUploadTests(TestCase):

    def test_file_upload(self):
        response = self.client.post(reverse('upload'), {'file': open('test_file.txt', 'rb')})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UploadedFile.objects.filter(name='test_file.txt').exists())

    def test_file_list(self):
        response = self.client.get(reverse('file_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ftp_app/file_list.html')