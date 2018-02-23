from django.db import models

# Create your models here.
from product.models import Product
from userProfile.models import UserProfile


class Rating(models.Model):
    """
    rating
        ----
        id PK int AUTOINCREMENT
        rated_by int FK >-< userProfile.id
        product int FK >- product.id
        rating int
    """
    SCORE_CHOICES = zip(range(1, 6), range(1, 6))
    rated_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES)

    def __str__(self):
        return "%s rating for %s by %s" % (self.rating, self.product, self.rated_by)
