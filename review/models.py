from django.db import models
import uuid as uuid_lib
# Create your models here.
from product.models import Product
from userProfile.models import UserProfile


class Review(models.Model):
    """
            ----
        id int PK AUTOINCREMENT
        author int FK >-< userProfile.id
        product int FK >-< product.id
        comments VCHAR(2000)?
        uuid uuid?
    """
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    def __str__(self):
        return "Review of %s on %s" % (self.author, self.product)
