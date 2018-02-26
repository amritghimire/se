from django import template

from relationship_app.models import Relationship

register = template.Library()


@register.filter
def display_review_count(o):
    return Relationship.objects.filter(product=o, review__isnull=True).count()


@register.filter
def display_recommend_count(o):
    return Relationship.objects.filter(product=o, recommended=True).count()
