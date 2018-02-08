from django.db import models

# Create your models here.
class Name(models.Model):
    name_text = models.CharField(max_length=20,help_text="Enter your Name")

    def __str__(self):
        return self.name_text
class Slug(models.Model):
    slug_text = models.CharField(max_length=200)

    def __str__(self):
        return self.slug_text
class Summary(models.Model):
    summary_text = models.CharField(max_length=20,help_text="Write Summary")

    def __str__(self):
        return self.summary_text
class Description(models.Model):
    description_text = models.CharField(max_length=20,help_text="Write Description")

    def __str__(self):
        return self.description_text
class Id(models.Model):
    id_detail = models.IntegerField(help_text="Enter your id")

class Image_for_detail(models.Model):
    image = models.ImageField()

