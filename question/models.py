from django.db import models

from category.models import Category
from userProfile.models import UserProfile


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
    # TODO: add relation to tag
    # tag=models.ManyToManyField(Tag)
    # TODO: add relation to Product
    # options = models.ManyToManyField(Product)
    upvoted_by = models.ManyToManyField(UserProfile)
    downvoted_by = models.ManyToManyField(UserProfile)
