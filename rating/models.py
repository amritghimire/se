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
    rated_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
