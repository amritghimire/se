from django.db import models

from category.models import Category
from product.models import Product
from tag.models import Tag
from userProfile.models import UserProfile
import uuid as uuid_lib


class Question(models.Model):
    """
            ----
        id PK int AUTOINCREMENT
        title VARCHAR(255)
        asked_by int FK >- userProfile.id
        summary string NULL
        category int FK >-< category.id
        tag int FK >- tag.id
        options int FK >-< product.id
        upvoted_by int FK >-< userProfile.id
        downvoted_by int FK >-< userProfile.id
    """
    title = models.CharField(max_length=255, help_text="Enter the title of question.")
    asked_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    summary = models.CharField(max_length=1024, null=True, blank=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    options = models.ManyToManyField(Product)
    upvoted_by = models.ManyToManyField(UserProfile, related_name='upvoted')
    downvoted_by = models.ManyToManyField(UserProfile, related_name='downvoted')
    slug = models.SlugField()
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
