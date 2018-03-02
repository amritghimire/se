import os

from django.conf import settings
from django.shortcuts import render
from os.path import isfile, join
from category_app.views import select_category_user_view
from tag.views import select_tag_user_view
from product_app.models import Product
from .utils import add_relationship_for_user, recalculate_score_product, recalculate_score_question
from relationship_app.models import Relationship, RelationshipWithQuestion
from userProfile_app.models import UserProfile


def index(request):
    if request.user.is_authenticated:
        user = request.user  # type: UserProfile
        if not user.selected_category.count():
            return select_category_user_view(request)
        if user.selected_tag.count() == 0:
            return select_tag_user_view(request)
        if Relationship.objects.filter(author=user).count() == 0:
            add_relationship_for_user(user)
        for relation in Relationship.objects.filter(score=0, author=user):
            print(relation)
            score = recalculate_score_product(user, relation)
            relation.score = score
            relation.save()
        for relation in RelationshipWithQuestion.objects.filter(score=0, author=user):
            relation.score = recalculate_score_question(user, relation.question)
            print(relation.score)
            relation.save()

        recommended_objects = [a.product for a in
                               Relationship.objects.filter(author=request.user).order_by('-score')[:5]]
        recommended_questions = [a.question for a in
                                 RelationshipWithQuestion.objects.filter(author=request.user).order_by('-score')[:5]]
    else:
        recommended_objects = [a.product for a in Relationship.objects.all()[:5]]
        recommended_questions = [a.question for a in RelationshipWithQuestion.objects.all()[:5]]

    recently_added = Product.objects.order_by('updated_at', 'created_at')[:5]

    context = {
        'recommended_objects': recommended_objects,
        'recommended_questions': recommended_questions,
        'recently_added': recently_added
    }

    return render(request, 'bridge_app/index.html', context=context)


def home(request):
    directory_to_scan = os.path.join(settings.BASE_DIR, "templates", "bridge_app")
    onlyfiles = [f for f in os.listdir(directory_to_scan) if isfile(join(directory_to_scan, f))]
    onlyfiles.remove("home.html")
    context = {
        "files": onlyfiles
    }
    return render(request, 'bridge_app/home.html', context=context)


def template(request, template_name="base"):
    return render(request, 'bridge_app/' + template_name)
