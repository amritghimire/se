import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from os.path import isfile, join

from product_app.models import Product
from userProfile_app.models import UserProfile


@login_required()
def index(request):
    user = request.user  # type: UserProfile
    selected_category = [a.uuid for a in user.selected_category.all()]
    recommended_objects = Product.objects.annotate(
        recommended_count=Count('recommended')/2).order_by('-recommended_count').filter(
        category__in=user.selected_category.all()).distinct()
    context = {
        'user': user,
        'recommended_objects': recommended_objects
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
