from django.db import models
import uuid as uuid_lib

from category.models import Category


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
    category = models.ManyToManyField(Category)
    # TODO: ManytoMany field tag
    # tag = models.ManyToManyField(Tag)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    product_picture = models.ImageField(upload_to="image/product")

