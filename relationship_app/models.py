from django.db import models
import uuid as uuid_lib
from product_app.models import Product
from userProfile_app.models import UserProfile


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
    review = models.TextField(blank=True, null=True)
    recommended = models.NullBooleanField(blank=True)

    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    def __str__(self):
        return "%s score for %s by %s" % (self.score, self.product, self.author)

    def recalculate_score(self):
        """
        :return int:
        """
        score_under_calculation = 0
        author_selected_category = [a.uuid for a in self.author.selected_category.all()]
        author_selected_tag = [a.uuid for a in self.author.selected_tag.all()]
        score_under_calculation += sum([10 for a in self.product.category.all() if a.uuid in author_selected_category])
        score_under_calculation += sum([5 for a in self.product.tag.all() if a.uuid in author_selected_tag])
        score_under_calculation += sum([4 for a in self.product.tag.all() if self.author in a.viewed.all()])
        if self.recommended is None:
            pass
        elif self.recommended:
            score_under_calculation += 7
        else:
            score_under_calculation -= 7
        if self.rating:
            score_under_calculation += 2
        if self.review:
            score_under_calculation += 2

        return score_under_calculation

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.score = self.recalculate_score()
        super().save(force_insert, force_update, using, update_fields)
