from django.db import models

from category_app.models import Category
from product_app.models import Product
from tag.models import Tag
from userProfile_app.models import UserProfile
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
    category = models.ManyToManyField(Category, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    options = models.ManyToManyField(Product, blank=True)
    upvoted_by = models.ManyToManyField(UserProfile, related_name='upvoted', blank=True)
    downvoted_by = models.ManyToManyField(UserProfile, related_name='downvoted', blank=True)
    slug = models.SlugField()
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        from relationship_app.models import RelationshipWithQuestion

        super().save(force_insert, force_update, using, update_fields)
        for user in UserProfile.objects.all():
            relationship = RelationshipWithQuestion(author=user, question=self)
            relationship.save()
