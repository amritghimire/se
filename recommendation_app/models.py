from django.db import models

# Create your models here.
from product_app.models import Product
from userProfile_app.models import UserProfile


class Recommended(models.Model):
    """
    recommendation
        --------
        id int PK AUTOINCREMENT
        recommended boolean
        author int FK >-< userProfile.id
        product int FK -< product.id
    """
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "%s recommended by %s" % (self.product, self.author)


class NotRecommended(models.Model):
    """
    recommendation
        --------
        id int PK AUTOINCREMENT
        recommended boolean
        author int FK >-< userProfile.id
        product int FK -< product.id
    """
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "%s not recommended by %s" % (self.product, self.author)

