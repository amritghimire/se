from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid as uuid_lib


class UserProfile(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=2)
    website = models.URLField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile/", null=True)
