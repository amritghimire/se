from django.db import models
import uuid as uuid_lib
from product.models import Product
from userProfile.models import UserProfile


class Relationship(models.Model):
    """
    relationship
        ----
        id PK int AUTOINCREMENT
        rated_by int FK >-< userProfile.id
        product int FK >- product.id
        rating int
    """
    SCORE_CHOICES = zip(range(1, 6), range(1, 6))
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True, editable=False)
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, null=True, blank=True)
    review = models.TextField()

    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    def __str__(self):
        return "%s rating for %s by %s" % (self.rating, self.product, self.author)
