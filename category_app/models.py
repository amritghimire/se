from django.db import models
import uuid as uuid_lib


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, help_text="Enter name of category")
    slug = models.SlugField()
    summary = models.CharField(max_length=200, help_text="Write Summary", null=True, blank=True)
    description = models.CharField(max_length=2000, help_text="Write Description", null=True, blank=True)
    image = models.ImageField(upload_to="image/category/", null=True, blank=True)
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
