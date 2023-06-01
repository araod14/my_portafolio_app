from django.test import TestCase
from django.urls import reverse
from .models import Project
from datetime import date

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un objeto Project para utilizar en las pruebas
        Project.objects.create(title="Test project", description="This is a test project", image="project.jpg", url="http://testproject.com", date=date.today())

    def test_title_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_framework_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('framework').verbose_name
        self.assertEqual(field_label, 'framework')

    def test_database_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('database').verbose_name
        self.assertEqual(field_label, 'database')

    def test_image_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_url_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'url')

    def test_date_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_title_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('description').max_length
        self.assertEqual(max_length, 250)

    def test_object_name_is_title(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.title}'
        self.assertEqual(expected_object_name, str(project))

    def test_upload_to_path(self):
        project = Project.objects.get(id=1)
        upload_to = project.image.field.upload_to
        self.assertEqual(upload_to, 'portfolio/images')


