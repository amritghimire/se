from django.db import models

# Create your models here.
from product.models import Product
from userProfile.models import UserProfile


class Recommendation(models.Model):
    """
    recommendation
        --------
        id int PK AUTOINCREMENT
        recommended boolean
        author int FK >-< userProfile.id
        product int FK -< product.id
    """
    recommended = models.BooleanField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
