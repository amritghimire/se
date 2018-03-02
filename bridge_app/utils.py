from product_app.models import Product
from question_app.models import Question
from relationship_app.models import Relationship
from userProfile_app.models import UserProfile


def add_relationship_for_user(user: UserProfile):
    for product in Product.objects.all():
        relationship = Relationship(author=user, product=product, review=None, rating=None, recommended=None)
        relationship.save()
    for question in Question.objects.all():
        relationship = Relationship(author=user, product=question)
        relationship.save()


def recalculate_score_product(author, r):
    """
    :return int:
    """
    # score_under_calculation = 0
    # r = Relationship.objects.get_or_create(author=author, product=product)
    product = r.product
    author_selected_category = [a.uuid for a in author.selected_category.all()]

    author_selected_tag = [a.uuid for a in author.selected_tag.all()]
    score_under_calculation = sum([10 for a in product.category.all() if a.uuid in author_selected_category])
    print(score_under_calculation)

    score_under_calculation += sum([5 for a in product.tag.all() if a.uuid in author_selected_tag])
    score_under_calculation += sum([4 for a in product.tag.all() if author in a.viewed.all()])
    if r.recommended is None:
        pass
    elif r.recommended:
        score_under_calculation += 7
    else:
        score_under_calculation -= 7
    if r.rating:
        score_under_calculation += 2
    if r.review:
        score_under_calculation += 2

    return score_under_calculation


def recalculate_score_question(author, question):
    """
    :return int:
    """
    score_under_calculation = 0
    author_selected_category = [a.uuid for a in author.selected_category.all()]
    author_selected_tag = [a.uuid for a in author.selected_tag.all()]
    score_under_calculation += sum([10 for a in question.category.all() if a.uuid in author_selected_category])
    score_under_calculation += sum([5 for a in question.tag.all() if a.uuid in author_selected_tag])
    score_under_calculation += sum([4 for a in question.tag.all() if author in a.viewed.all()])

    return score_under_calculation
