from django.db import models
import uuid as uuid_lib

from userProfile.models import UserProfile


class Tag(models.Model):
    """
            ---
        id PK int AUTOINCREMENT
        tag_name VARCHAR(200)
        viewed int
        slug VARCHAR(200)
        uuid uuid?
    """
    name = models.CharField(max_length=200)
    viewed = models.ManyToManyField(UserProfile, related_name='viewed_tag')
    slug = models.SlugField()
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    selected_by = models.ManyToManyField(UserProfile, related_name='selected_tag')
