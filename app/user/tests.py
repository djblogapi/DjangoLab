from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from six import BytesIO

from user.models import File


def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    """
    Generate a test image, returning the filename that it was saved as.

    If ``storage`` is ``None``, the BytesIO containing the image data
    will be passed instead.
    """
    data = BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


def generate_test_image():
    # Create a simple black image (100x100 pixels) for testing
    image = Image.new('RGB', (100, 100), 'black')
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    return SimpleUploadedFile('test_image.jpg', buffer.getvalue(), content_type='image/jpeg')


class FileViewSetTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', email="testeamil@test.t", password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_file_upload(self):
        file_data = {'image': generate_test_image()}
        response = self.client.post(reverse('v1:user:file-list'), data=file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verify that the file has been saved in the database
        self.assertEqual(File.objects.count(), 1)

    def test_file_upload_invalid_format(self):
        file_data = {
            'image': SimpleUploadedFile('invalid_file.txt', b'file_content', content_type='text/plain')
        }

        response = self.client.post(reverse('v1:user:file-list'), data=file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('image', response.data)

        # Verify that the file has not been saved in the database
        self.assertEqual(File.objects.count(), 0)

    def test_file_upload_invalid_size(self):
        file_data = {
            'image': SimpleUploadedFile('large_image.jpg', b'file_content' * 1024 * 1024 * 20,
                                        content_type='image/jpeg')
        }

        response = self.client.post(reverse('v1:user:file-list'), data=file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('image', response.data)

        # Verify that the file has not been saved in the database
        self.assertEqual(File.objects.count(), 0)
