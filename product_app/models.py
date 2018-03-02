from django.db import models
import uuid as uuid_lib

from category_app.models import Category
# from recommendation.models import Recommendation
from tag.models import Tag
from userProfile_app.models import UserProfile


class Product(models.Model):
    """
        Product model
        ------
        id PK int AUTOINCREMENT
        product_name VARCHAR(200)
        category int FK >-< category.id
        tag int FK >- tag.id
        manufacturer VARCHAR(200)
        releaseDate date?
        upvoted_by int FK >-< userProfile.id
        downvoted_by int FK >-< userProfile.id
        product_picture VARCHAR(100)
    """
    title = models.CharField(max_length=254)
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    category = models.ManyToManyField(Category, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    summary = models.TextField(null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ManyToManyField(UserProfile, blank=True)
    release_date = models.DateField(null=True, blank=True)
    product_picture = models.ImageField(upload_to="image/product", null=True, blank=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        from relationship_app.models import Relationship

        super().save(force_insert, force_update, using, update_fields)
        for user in UserProfile.objects.all():
            relationship = Relationship(author=user, product=self, review=None)
            relationship.save()
