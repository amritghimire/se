from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid as uuid_lib

from category_app.models import Category


class UserProfile(AbstractUser):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
        ('U', "Unspecified")
    )
    dob = models.DateField(null=True, blank=True)
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER)
    website = models.URLField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="image/profile/", null=True, blank=True)
    selected_category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
