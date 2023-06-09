from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    framework = CharField(max_length=50, blank=True, null=True)
    database = CharField(max_length=50, blank=True, null=True)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title
