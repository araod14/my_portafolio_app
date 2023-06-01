from django.test import TestCase
from .models import Post
import datetime

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un objeto Post para utilizar en las pruebas
        Post.objects.create(title="Test post", description="This is a test post", date=datetime.date.today())

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_image_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_date_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_str_method(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), "Test post")

    def test_image_upload_path(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.image.field.upload_to, "blog/images")

    def test_date_default_value(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.date, datetime.date.today())
